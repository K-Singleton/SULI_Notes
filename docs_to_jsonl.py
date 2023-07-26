# Here is an example of a line in the jsonl file
# {"text": "### Human: Hola### Assistant: \u00a1Hola! \u00bfEn qu\u00e9 puedo ayudarte hoy?"}
import json
import pathlib

def main():
    questions = {
        '../kb_sdk_docs/source/howtos/add_ui_elements.rst': 'How do I add a ui element to a KBase module?',
        '../kb_sdk_docs/source/howtos/create_a_report.rst': 'How do I create a report for a KBase app?',
        '../kb_sdk_docs/source/howtos/dynamic_services.rst': 'How do I create a dynamic service for an SDK module?',
        '../kb_sdk_docs/source/howtos/edit_your_dockerfile.rst': 'How do I edit the dockerfile of a KBase app?',
        '../kb_sdk_docs/source/howtos/file_utils.rst': 'How do I acess the utilities of a file?',
        '../kb_sdk_docs/source/howtos/fill_out_app_information.rst': 'How do I complete the documentation for a KBase app?',
        '../kb_sdk_docs/source/howtos/job_manager.rst': 'How do I list and view the jobs running on KBase?',
        '../kb_sdk_docs/source/howtos/manual_build.rst': 'How do I manually build the KBase SDK?',
        '../kb_sdk_docs/source/howtos/run_a_shell_command.rst': 'How do I run shell commands in the dockerfile of a KBase app?',
        '../kb_sdk_docs/source/howtos/update_to_py3.rst': 'How do I update a KBase module to Python 3?',
        '../kb_sdk_docs/source/howtos/workspace.rst': 'How do I add reference data to a KBase app?',
        '../kb_sdk_docs/source/howtos/work_with_reference_data.rst': 'How do I retrieve the workspace object from a KBase narrative?',
    }

    kbase_files = pathlib.Path("../kb_sdk_docs/source/howtos")
    howtos = (list(kbase_files.iterdir()))
    
    with open("data.jsonl","w") as f:
        pass
    for howto in howtos:
        with open(howto) as f:
            answer = f.read()
        text = f'### Human: {questions[str(howto)]}### Assistant: {answer}'
        # dict(foo=100, bar=200)
        line = json.dumps(dict(text=text))
        with open("data.jsonl","a") as f:
            f.write(f'{line}\n')
   
if __name__ == "__main__":
    main()
