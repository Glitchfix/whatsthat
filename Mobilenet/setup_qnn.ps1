# setup_qnn.ps1
                    
py -3.10 -m venv QAIRT_VENV
& "QAIRT_VENV\Scripts\Activate.ps1" 
# upgrade pip
python -m pip install --upgrade pip
                    
#update the QNN version in the below command as needed. 
& C:\Qualcomm\AIStack\QAIRT\2.24.0.240626\bin\envsetup.ps1
pip install psutil==6.0.0 
python "${QNN_SDK_ROOT}\bin\check-python-dependency"
& "${QNN_SDK_ROOT}\bin\check-windows-dependency.ps1"
                    
pip install tensorflow==2.10.1 
pip install tflite==2.3.0
pip install torch==1.13.1
pip install torchvision==0.14.1 
pip install onnx==1.12.0
pip install onnxruntime==1.17.1
pip install onnxsim==0.4.36 
                    
cd "${QNN_SDK_ROOT}"