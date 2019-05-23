![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

# Darknet #
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

# Hướng dẫn khai thác dữ liệu từ COCO #

1. Chuẩn bị dữ liệu COCO

**[Ubuntu/Linux]** Free-to-run
  
  Từ thư mục darknet chạy lệnh 
  > $ sh scripts/get_coco_dataset.sh

**[Windows]** Yêu cầu các phần mềm như GitSCM, 7Zip
  
  1.1.  Tạo thư mục "coco" và thư mục "images" theo đường dẫn "darknet/scripts/coco/images"
  
  1.2.  Trong thư mục "images" vừa tạo, tải 2 file sau và giải nén:
  
          + https://pjreddie.com/media/files/train2014.zip
          
          + https://pjreddie.com/media/files/val2014.zip
          
  1.3.  Trở lại thư mục "coco", tải các file sau và giải nén:
  
          + https://pjreddie.com/media/files/instances_train-val2014.zip  <== File quan trọng
          
          + https://pjreddie.com/media/files/coco/5k.part
          
          + https://pjreddie.com/media/files/coco/trainvalno5k.part
          
          + https://pjreddie.com/media/files/coco/labels.tgz              <== File quan trọng
          
  1.4.  Kiểm tra 2 file sau (được đính kèm) trong thư mục "coco": (2 file này sẽ được sinh tự động trong đoạn script get_coco_dataset.sh nếu bạn sử dụng Ubuntu/Linux)
  
          + 5k.txt
          
          + trainvalno5k.txt

2. Chạy ví dụ cách khai thác dữ liệu COCO tại đường dẫn "darknet/PythonExample" 
  + LoadPerson.ipynb  => Mã nguồn (kèm chú thích) ví dụ cách đọc, trích xuất và hiển thị dữ liệu
  + SpUtils.py => Hàm vẽ khung chữ nhật quanh đối tượng
    
