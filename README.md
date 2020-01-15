<h1 align="center">
  <img src="icons/lena.png"><br/>Cut And Save Faces
</h1>

<h4 align="center">
Face pic collecting tool
</h4>

<div align="center">
  <a href="https://github.com/Jaesung-Jun/Cut-And-Save-Faces/releases"><img src="https://img.shields.io/badge/release-1.3--GUI-blue"></a>
  <br>
  <a href="https://pypi.org/project/PyQt5/"><img src="https://img.shields.io/badge/PyQt5-5.13.0-green"></a>
  <a href="https://pypi.org/project/opencv-python/"><img src="https://img.shields.io/badge/opencv--python-4.1.0.25-green"></a>
  <a href="https://pypi.org/project/opencv-contrib-python/"><img src="https://img.shields.io/badge/opencv--contrib--python-4.1.0.25-green"></a>
  <a href="https://pypi.org/project/dlib/"><img src="https://img.shields.io/badge/dlib-19.17.0-green"></a>
  <a href="https://pypi.org/project/imutils/"><img src="https://img.shields.io/badge/imutils-0.5.2-green"></a>
  <br>
  <a href="https://raw.githubusercontent.com/Jaesung-Jun/Cut-And-Save-Faces/master/LICENSE"><img src="https://img.shields.io/badge/licence-MIT-lightgrey"></a>
</div>

## Description
Cut And Save Faces is pictures collecting tool.<br>
Written by Python. (uses Qt to develop its graphical interface)
<div align="center">
<img src="https://raw.githubusercontent.com/Jaesung-Jun/Cut-And-Save-Faces/master/imgs/gui.png" width=500/>
<h5> Input </h5>
<img src="https://raw.githubusercontent.com/Jaesung-Jun/Cut-And-Save-Faces/master/sample/red_velvet.jpg" width=200 />
<br>
<h5> Output (used haarcascade_frontalface_default.xml)</h5>
<img src="https://raw.githubusercontent.com/Jaesung-Jun/Cut-And-Save-Faces/master/sample/sample_outputs/red_velvet.jpg_0_cropped.jpg" width=80/>
<img src="https://raw.githubusercontent.com/Jaesung-Jun/Cut-And-Save-Faces/master/sample/sample_outputs/red_velvet.jpg_1_cropped.jpg" width=80/>
<img src="https://raw.githubusercontent.com/Jaesung-Jun/Cut-And-Save-Faces/master/sample/sample_outputs/red_velvet.jpg_2_cropped.jpg" width=80/>
<img src="https://raw.githubusercontent.com/Jaesung-Jun/Cut-And-Save-Faces/master/sample/sample_outputs/red_velvet.jpg_3_cropped.jpg" width=80/>
<img src="https://raw.githubusercontent.com/Jaesung-Jun/Cut-And-Save-Faces/master/sample/sample_outputs/red_velvet.jpg_4_cropped.jpg" width=80/>
</div>

## Features
* [ ] support video files
* [x] Face Alignment
* [x] Graphic InterFace
* [ ] Labeling
  
## Requirements

* Ubuntu(Not tested) , macOS(Not tested), Windows
* PyQt5
* Python 3 

## Installation

### dlib install guide

```bash
# You can see dlib install guide at
# https://www.learnopencv.com/install-dlib-on-windows/
```
### Require libraries install
```bash
# opencv-python, opencv-contrib-python, dlib, imutils, PyQt5
# Please note dlib install guide
#
# Develop Environment
#
#  ●  opencv-python==4.1.0.25
#  ●  opencv-contrib-python==4.1.0.25
#  ●  dlib==19.17.0
#  ●  imutils==0.5.3
#  ●  PyQt5==5.14.1
#
# Probably, CASF can be executed with higher versions of libraries.
#
$ pip install opencv-python
$ pip install opencv-contrib-python
$ pip install imutils
$ pip install PyQt5
```

### Execution
```bash
$ python CASF-Main.py
```

## Usage

<div align="center">

<img src="https://raw.githubusercontent.com/Jaesung-Jun/Cut-And-Save-Faces/master/imgs/guide.PNG" width=500/>

</div>

* **(1)** : Select your input path (dataset's path that you want to save&cut )
* **(2)** : Select path where you want to save
* **(3)** : Select output data type you want to save (or select your own detection file)
* **[Option] (3-2)** : select Options
* **(4)** Run

## References
+ **XML & dat Files Reference**
  * https://github.com/opencv/opencv/blob/master/data/
  * https://github.com/nagadomi/lbpcascade_animeface
  * https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat
+ **Copyrights**
  * Copyright (C) 2000-2020, Intel Corporation, all rights reserved.
  * Copyright (C) 2009-2011, Willow Garage Inc., all rights reserved.
  * Copyright (C) 2009-2016, NVIDIA Corporation, all rights reserved.
  * Copyright (C) 2010-2013, Advanced Micro Devices, Inc., all rights reserved.
  * Copyright (C) 2015-2016, OpenCV Foundation, all rights reserved.
  * Copyright (C) 2015-2016, Itseez Inc., all rights reserved.
  * Copyright (C) 2019-2020, Xperience AI, all rights reserved.
  * Third party copyrights are property of their respective owners.
  * *Please note https://github.com/opencv/opencv/blob/master/LICENSE before using this software.*



