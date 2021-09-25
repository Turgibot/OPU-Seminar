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

echo Article 1

manim StereoVisionArticle.py StereoModelTitle
manim StereoVisionArticle.py StereoCorrespondence1
manim StereoVisionArticle.py StereoCorrespondence2
manim StereoVisionArticle.py StereoCorrespondence3
manim StereoVisionArticle.py StereoCorrespondence4
manim StereoVisionArticle.py StereoCorrespondence5

echo uploading to github

cd ..
git add .
git commit -m "uploading from script"
git push