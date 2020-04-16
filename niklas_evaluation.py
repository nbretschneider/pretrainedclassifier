# Evaluation of Results (evaluation of uploaded_images):

#	1) Yes, all three correctly identified the breed of the dog, a Dalmatian in this case (Dog_01)
#	2) Yes, all three correctly identified the breed of the dog, a Dalmatian in this case, consistent with Dog_01
#	3) Yes, all three correctly noticed that both pictures are not dogs
#	4) All three tools worked really well overall. However, AlexNet did one misidentification, it classified a house as picket fence. Looking at runtime, ResNet and AlexNet ran the script in 10 seconds, while VGG took 13 seconds. Therefore, I would recommend to use ResNet (100% correct identification + fastest runtime. However, the analysis in the previous lesson (showing VGG as best model architecture) are also valid and should be considered in a final recommendation. 