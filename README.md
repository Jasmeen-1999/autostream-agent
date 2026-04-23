# 🤖 AutoStream Conversational AI Agent

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![AI](https://img.shields.io/badge/AI-Agentic%20System-purple.svg)
![RAG](https://img.shields.io/badge/RAG-Knowledge%20Retrieval-green.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen.svg)

## Overview

AutoStream Conversational AI Agent is a modular agentic AI system built for a SaaS platform that provides automated video editing tools.

The agent simulates a real-world AI assistant capable of understanding user intent, answering product queries using a knowledge base (RAG), maintaining multi-turn conversation memory, and capturing high-intent leads through tool execution.

This project demonstrates a structured **agent-based architecture inspired by production-level AI systems**.

## Features

- Intent detection (greeting, product query, high-intent lead)
- RAG-based responses using a local knowledge base
- Multi-turn conversation memory
- Lead capture workflow with tool execution
- Modular and scalable agent architecture

## Architecture

User Input → app.py → Intent Detection (utils/intent.py) → graph.py → {RAG System / Tool Execution / Direct Response} → Final Output

The system follows a modular pipeline where:

- Intent detection classifies user input
- Graph router decides execution path
- RAG system retrieves knowledge from a local JSON file
- Tools module handles lead capture actions
- State is maintained across conversation turns using a dictionary-based memory system

## How to Run

Clone the repository:
