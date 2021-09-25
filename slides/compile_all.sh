#!/bin/sh
echo Compiling all manim animation and uploading to website

manim Introduction.py Title
manim StereoVision.py StereoVision
manim StereoVision.py WhatIsEventCameraPart1
manim StereoVision.py WhatIsEventCameraPart2
manim StereoVision.py WhatIsEventCameraPart3
manim StereoVision.py WhatIsEventCameraPart4
manim StereoVision.py WhatIsEventCameraPart5
manim StereoVision.py Football
manim StereoVision.py Visualization
manim StereoVision.py EventModelPart1
manim StereoVision.py EventModelPart2
manim StereoVision.py EventModelPart3
manim StereoVision.py EventModelPart4
manim StereoVision.py EventModelPart5

echo End of introduction

echo uploading to github

cd ..
git add .
git commit -m "uploading from script"
git push