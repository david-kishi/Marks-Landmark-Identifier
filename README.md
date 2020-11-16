# Mars Landmark Identifier
Identifying Mars landmarks type utilizing Convolutional Neural Networks.
[Presentation](https://docs.google.com/presentation/d/1zVyXnglQqo3rK-XTpM5fgbpxNQfJvr6nINTiRKdAer4/edit?usp=sharing)

## Description
The Mars Landmark Identifier (MLI), utilizes computer vision to identify the type of landmark currently being looked at using a trained convolutional neural network. The dataset used to train the model was NASA's Mar's Orbiter HiRISE images, which NASA has already deduced down to several category types. (Dataset info and source can be referred to below)

## What's next for MLI
The next objective for MLI is to transition from an image classification model to an object detection model, which would be able to detect multiple types of landmarks in one image. The issue with the image classification model is at times there will be more than one type of landmark in view, which confuses the model.

## Dataset
Mars orbital image (HiRISE) labeled data set version 3<br>
[ [NASA Open Data Portal](https://data.nasa.gov/Space-Science/Mars-orbital-image-HiRISE-labeled-data-set-version/egmv-36wq), [Data Source](https://zenodo.org/record/2538136#.Xj8DgFJKhZo), DOI: 10.5281/zenodo.2538136 ]

| **Category**  	| **Count** |
|---------------	|---------	|
| other         	| 61054   	|
| crater        	| 4900    	|
| dark dune     	| 1141    	|
| slope streak  	| 2331    	|
| bright dune   	| 1750    	|
| impact ejecta 	| 231     	|
| swiss cheese  	| 1148    	|
| spider        	| 476     	|



## Contact
David Nguyen - david@knytes.com
