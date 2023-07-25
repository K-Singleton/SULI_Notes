# Here is an example of a line in the jsonl file
# {"text": "### Human: Hola### Assistant: \u00a1Hola! \u00bfEn qu\u00e9 puedo ayudarte hoy?"}
import json
import pathlib

def main():
    howto_dict = {}
    howto_dict['../kb_sdk_docs/source/howtos/add_ui_elements.rst'] = 'How do I add a ui element to a KBase module?'
    howto_dict['../kb_sdk_docs/source/howtos/create_a_report.rst'] = 'How do I create a report for a KBase app?'
    howto_dict['../kb_sdk_docs/source/howtos/dynamic_services.rst'] = 'How do I create a dynamic service for an SDK module?'
    howto_dict['../kb_sdk_docs/source/howtos/edit_your_dockerfile.rst'] = 'How do I edit the dockerfile of a KBase app?'

    howto_dict['../kb_sdk_docs/source/howtos/file_utils.rst'] = 'value1'
    howto_dict['../kb_sdk_docs/source/howtos/fill_out_app_information.rst'] = 'value1'
    howto_dict['../kb_sdk_docs/source/howtos/job_manager.rst'] = 'value1'
    howto_dict['../kb_sdk_docs/source/howtos/manager_build.rst'] = 'value1'

    howto_dict['../kb_sdk_docs/source/howtos/run_a_shell_command.rst'] = 'value1'
    howto_dict['../kb_sdk_docs/source/howtos/update_to_py3.rst'] = 'value1'
    howto_dict['../kb_sdk_docs/source/howtos/workspace.rst'] = 'value1'
    howto_dict['../kb_sdk_docs/source/howtos/work_with_reference_data.rst'] = 'value1'

    kbase_files = pathlib.Path("../kb_sdk_docs/source/howtos")
    howtos = (list(kbase_files.iterdir()))
    
    with open("data.jsonl","w") as f:
        pass
    for howto in howtos:
        with open(howto) as f:
            answer = f.read()
        for key,value in howto_dict.items():
            text = f'### Human: {key}### Assistant: {value}'
        # dict(foo=100, bar=200)
            line = json.dumps(dict(text=text))
        with open("data.jsonl","a") as f:
            f.write(f'{line}\n')
   
if __name__ == "__main__":
    main()
