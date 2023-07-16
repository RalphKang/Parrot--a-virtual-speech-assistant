![mockingbird](https://github.com/RalphKang/Parrot--a-virtual-speech-assistant/blob/master/utilities_readme/microphone.jpg)


[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

> English
## Introduction
Parrot is an open-source personal virtual assistant based on GPT-3.5, you can talk with it like you are using Siri or any other similar virtual assistant.
It has the following features.

🤩 **Speech in, Speech Out** You can talk with AI agent with your voice, and it will also talk with you as feedback. 

🤩 **Wake it up with the name you like** You can wake your parrot with any name you given to it, for example, I named it "Ralph", then I can wake "Ralph" up with saying "Hi, Ralph". Similarly, one can name it "Judy","Fox", etc.

🤩 **Stop and re-wake up** You can stop it with the word of "stop", "quit", etc. and re-wake it up with calling its name.

## Quick Start

### 1. Install Requirements
* Create a environment with python 3.10 (as we test on this environment)
 
  ```conda env create -n env_name python==3.10```
* Then activate the environment
  
  ```conda activate env_name```
* Finally, install all dependencies via
  
  ```pip install -r requirements.txt```

Now you can play with it.

### 2. Configuration
* Please copy the **args.json** file and rename the copy as **args_private.json**. This operation is used to avoid any leakage of your personal information, as the args_private file will not be saved by git.

* Then open **args_private.json**, input your openai key and the agent name you want to give. In order to avoid the accent issue, please write several names similar to the pronunciation of your wanted name, for example:
  
  `"agent_name": ["Ralph", "Raph", "Ralf", "ralph", "raph", "ralf"]`


### 3. Play
* run the project in the environment you created by:
  
   `python main_v2.py`
* Then your agent is activated, one hint is your microphone is activated:

![microphone](\\utilities_readme\\microphone.jpg)

* you can activate it via saying "Hi, Ralph" (suppose Ralph is the agent name)
* and talk to it then.
#### [DEMO VIDEO](https://www.bilibili.com/video/BV17Q4y1B7mY/)