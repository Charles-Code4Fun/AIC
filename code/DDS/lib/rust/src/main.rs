// src/main.rs

use serde_json::json;
use std::sync::{Arc, Mutex};
use warp::Filter;

mod blockchain;
use blockchain::Blockchain;

#[tokio::main]
async fn main() {
    let blockchain = Arc::new(Mutex::new(Blockchain::new()));

    let upload_route = {
        let blockchain = blockchain.clone();
        warp::post()
            .and(warp::path("upload_data"))
            .and(warp::body::json())
            .map(move |data: serde_json::Value| {
                let sender = data["sender"].as_str().unwrap().to_string();
                let data_content = data["data"].as_str().unwrap().to_string();

                let mut blockchain = blockchain.lock().unwrap();
                blockchain.new_transaction(sender.clone(), "marketplace".to_string(), data_content);
                let block = blockchain.new_block("previous_hash_example".to_string());

                warp::reply::json(&json!({
                    "message": "Data uploaded successfully",
                    "block_index": block.index,
                    "data": block.transactions,
                }))
            })
    };

    let get_data_route = {
        let blockchain = blockchain.clone();
        warp::get()
            .and(warp::path("get_data"))
            .map(move || {
                let blockchain = blockchain.lock().unwrap();
                warp::reply::json(&blockchain.chain())
            })
    };

    let access_data_route = {
        let blockchain = blockchain.clone();
        warp::get()
            .and(warp::path!("access_data" / usize))
            .map(move |block_index| {
                let blockchain = blockchain.lock().unwrap();
                if block_index < 1 || block_index > blockchain.chain.len() {
                    return warp::reply::with_status("Block not found", warp::http::StatusCode::NOT_FOUND);
                }
                let block = &blockchain.chain[block_index - 1];
                warp::reply::json(block)
            })
    };

    let routes = upload_route.or(get_data_route).or(access_data_route);

    warp::serve(routes).run(([0, 0, 0, 0], 3030)).await;
}
