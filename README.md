Potsdam Hospital Pathfinding Project

Overview

This project focuses on improving emergency routing efficiency in Potsdam, Germany by using graph based pathfinding algorithms.

The city road network is modeled as a graph, and shortest path algorithms are used to find the nearest hospital from different locations.

Objectives

Model Potsdam as a graph using real world map data

Identify hospital locations

Implement Dijkstra’s Algorithm and A* Algorithm

Compare performance (distance, runtime, memory)

Technologies Used

Python

OSMnx (for map data)

NetworkX (for graph algorithms) 

Time & tracemalloc (for performance measurement)

Algorithms

Dijkstra’s Algorithm

Finds the shortest path by exploring all possible routes.

A* Algorithm

Uses a heuristic to guide the search and improve efficiency.

Data

Hospitals

Klinikum Ernst von Bergmann

Alexianer St. Josefs-Krankenhaus

Protestant Center for Geriatric Medicine

Klinikum Westbrandenburg Standort Potsdam

Scenarios

Potsdam Hauptbahnhof

Innenstadt

Babelsberg

Universität Potsdam

Bornstedt

Results

Both algorithms produced the same shortest path in all scenarios.

A* was slightly faster in all cases, while Dijkstra used slightly less memory.

How to Run

Install dependencies:

pip install -r requirements.txt

Run the project:

python main.py

Project Structure

potsdam_hospital_pathfinding/
│
├── main.py
├── requirements.txt
└── README.md

Notes

This project uses real world data from OpenStreetMap and demonstrates how pathfinding algorithms can be applied to emergency routing problems.