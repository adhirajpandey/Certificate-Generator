# Certificate-Generator
This tool automates the process of making multiple certificates from canva template by using browser automation with playwright. 

GUI is built using pysimpleGUI.

It can be used by any Organization / College Society or Club where bulk certificates for participants is to be generated.


### Installing

1. Clone the repository to your machine using the following command:

    `git clone https://github.com/adhirajpandey/Certificate-Generator`


2. Once the repository is cloned, you can install the necessary packages by running the following command:

    `pip install -r requirements.txt`

    If facing any problem in Linux, `sudo bash install.sh`

### Running the application

To run the GUI of the application, execute the following command: `python main.py`

**🔴NOTE : Please ensure that your canva certificate template contains "Name Placeholder" where you want to enter participant's name.**

### Usage

1. Make the canva template and add "Name Placeholder" where required.
2. Create `names.txt` file and add names of all the candidates in there.
3. Run the application: `python main.py`
4. Browse names.txt file and fill canva template link and click SUBMIT.
5. Wait for the process to complete and then download the zip file of all the certificates.
6. Extract the Certificates into `certs` folder and then move that folder to the cloned repository
7. Move the names.txt file to the cloned repository.
8. Run `rename.py` to rename the downloaded certificate files.

**🟩NOTE : Watch the below linked sample demonstration to clearly understand the process**

## Features to be added

* Add option for getting any placeholder name instead of fixed "Name Placeholder".


## Screenshot

![image](https://user-images.githubusercontent.com/87516052/222500541-e0336617-2044-4b55-a33f-bfe7b54cb782.png)

## Demonstration

Youtube : https://youtu.be/B2F37C5_oU4
