import subprocess

llm_path = "C:\\Users\\QCWorkshop\\Downloads\\Team11\\llama-b3561-bin-win-llvm-arm64\\"

text_input = "Tell me about life."

inference_exe_filename = "llama-cli.exe"

llm_name = "Meta-Llama-3-8B-Instruct-Q4_K_M.gguf"

def generate_narrative(prompt=text_input, narrative_length=1):

    llm_path = "C:\\Users\\QCWorkshop\\Downloads\\Team11\\llama-b3561-bin-win-llvm-arm64\\"

    text_input = "Tell me about life."

    inference_exe_filename = "llama-cli.exe"

    llm_name = "Meta-Llama-3-8B-Instruct-Q4_K_M.gguf"

    # Define the command and its arguments
    command = [
        llm_path + inference_exe_filename,
        "-m", llm_path + llm_name,
        "-n", str(narrative_length),
        "-p", prompt
    ]

    # Run the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output
    output = "".join(result.stdout.split("\n")[1:])
    print(result.stdout)

# generate_narrative(prompt='''In this sentence does the user ask about any object or thing 
#                    by saying something like 'What is that' answer only a YES or a NO
                   
#                    INPUT: Can you tell me what do you see?

#                    OUTPUT_JSON_FORMAT: {'answer':'Yes or No'}
#                    ''')


generate_narrative(prompt="""I am a computer and I only understand 0 or 1, I want to know if user ask about any object/thing. Given a input respond either 0 or 1 only. 1 if it satisfies the condition else 0. Now tell me if user input is, "What is that" what is the ouput!
                   """, narrative_length=3)
generate_narrative(prompt="Explain me something about cat, and explain like I am a 5 year old", narrative_length=128)