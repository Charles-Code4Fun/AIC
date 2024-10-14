// src/blockchain.rs

use serde::{Deserialize, Serialize};
use serde_json::json;
use std::time::{SystemTime, UNIX_EPOCH};

#[derive(Serialize, Deserialize, Clone)]
struct Transaction {
    sender: String,
    recipient: String,
    data: String,
}

#[derive(Serialize, Deserialize)]
struct Block {
    index: usize,
    transactions: Vec<Transaction>,
    timestamp: u64,
    previous_hash: String,
}

#[derive(Default)]
pub struct Blockchain {
    chain: Vec<Block>,
    current_transactions: Vec<Transaction>,
}

impl Blockchain {
    pub fn new() -> Self {
        let mut blockchain = Blockchain::default();
        blockchain.new_block("1".to_string()); // Genesis block
        blockchain
    }

    pub fn new_block(&mut self, previous_hash: String) -> &Block {
        let block = Block {
            index: self.chain.len() + 1,
            transactions: self.current_transactions.clone(),
            timestamp: Self::current_timestamp(),
            previous_hash,
        };
        self.current_transactions.clear();
        self.chain.push(block);
        self.chain.last().unwrap()
    }

    pub fn new_transaction(&mut self, sender: String, recipient: String, data: String) {
        self.current_transactions.push(Transaction {
            sender,
            recipient,
            data,
        });
    }

    pub fn chain(&self) -> &Vec<Block> {
        &self.chain
    }

    fn current_timestamp() -> u64 {
        SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .expect("Time went backwards")
            .as_secs()
    }
}
