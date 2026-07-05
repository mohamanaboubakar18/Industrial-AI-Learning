# HV Substation Thermal Monitoring

A simple Python tool to monitor temperature sensors on high voltage substations and detect anomalies automatically.

## Why I built this

I worked 6 years as an electrical technician at Eneo Cameroon, maintaining HV substations. One of the things I noticed is that a lot of equipment failures start with temperature — and most of the time, nobody sees it coming because the data is there but nobody is really looking at it.

Now that I'm studying engineering at ENIB Brest, I wanted to start connecting what I learned on the field with what AI and Python can do. This project is a first step in that direction.

It's not a big project. But it's real — based on a real problem I've seen with my own eyes.

## What it does

- Takes temperature readings from multiple sensors on a HV substation
- Calculates the average and standard deviation
- Compares each reading to a critical alert threshold
- Prints a clear report in the terminal
- Generates a bar chart with anomalies highlighted in red
- Exports the chart as a PNG file

## How to run it

Make sure you have Python installed, then:

pip install matplotlib
python hta_thermal_monitoring.py

That's it.

## What I want to add next

- Load real data from a CSV file instead of hardcoded values
- Add a timestamp to each reading
- Maybe a simple machine learning model to predict failures before they happen


## About me

I'm Mohaman Aboubakar, electrical engineering student at ENIB Brest (France), originally from Cameroon. Before coming here I spend 6 years working on real HV substations — so when I build something, I try to make sure it actually make sense in the field, not just on paper.
