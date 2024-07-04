from ultralytics import YOLO

model =YOLO('/Users/priyansh/Desktop/Anti spoofing/yolov8n.pt')

def main() : 
    model.train(data='Dataset/SplitData/dataOffline.yaml', epochs = 2 )

if __name__ == '__main__' :
    main()