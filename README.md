# 🚑 Potsdam Hospital Pathfinding Project

## 📌 Overview
This project focuses on improving emergency routing efficiency in Potsdam, Germany using graph based pathfinding algorithms.

The city road network is modeled as a graph, and shortest path algorithms are used to determine the nearest hospital from different locations.

---

## 🎯 Objectives
- Model Potsdam as a graph using real world data  
- Identify hospital locations  
- Implement Dijkstra and A* algorithms  
- Compare performance (distance, runtime, memory)  

---

## ⚙️ Technologies Used
- Python  
- OSMnx (map data)  
- NetworkX (graph algorithms)  
- time & tracemalloc (performance measurement)  

---

## 🧠 Algorithms

### 🔹 Dijkstra’s Algorithm
Explores all possible paths to guarantee the shortest path.

### 🔹 A* Algorithm
Uses a heuristic (straight-line distance) to guide the search and improve efficiency.

---

## 🏥 Data

### Hospitals
- Klinikum Ernst von Bergmann  
- Alexianer St. Josefs-Krankenhaus  
- Protestant Center for Geriatric Medicine  
- Klinikum Westbrandenburg Standort Potsdam  

### Scenarios
- Potsdam Hauptbahnhof  
- Innenstadt  
- Babelsberg  
- Universität Potsdam  
- Bornstedt  

---

## 📊 Results
- Both algorithms found the same shortest path in all scenarios  
- A* was slightly faster  
- Dijkstra used slightly less memory  

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt