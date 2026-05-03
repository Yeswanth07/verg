# -*- coding: utf-8 -*-

import argparse
from pathlib import Path
import os
import re
import json

def to_pascal_case(name: str) -> str:
    """vergsample -> Vergsample | my-service -> MyService"""
    return ''.join(word.capitalize() for word in re.split(r'[-_\s]', name))

def to_camel_case(name: str) -> str:
    """vergsample -> vergsample | my-service -> myService"""
    pascal = to_pascal_case(name)
    return pascal[0].lower() + pascal[1:]

def to_lower(name: str) -> str:
    """my-service -> myservice"""
    return re.sub(r'[-_\s]', '', name).lower()

def to_upper(name: str) -> str:
    """orderservice -> ORDERSERVICE | my-service -> MY_SERVICE"""
    return re.sub(r'[-\s]', '_', name).upper()

def main():
    resourse_path = os.getcwd()+os.path.sep+"src"+os.path.sep+"main"+os.path.sep+"resources"
    registry_path = os.getcwd()+os.path.sep+"src"+os.path.sep+"main"+os.path.sep+"java"+os.path.sep+"com"+os.path.sep+"registry"+os.path.sep+"verg"
    util_path = os.getcwd()+os.path.sep+"src"+os.path.sep+"main"+os.path.sep+"java"+os.path.sep+"com"+os.path.sep+"registry"+os.path.sep+"verg"+os.path.sep+"core"+os.path.sep+"util"
    


    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    print(str(args.name).lower())
    
    if Path(registry_path+os.path.sep+args.name).is_dir() == False:

        '''Controller'''
        Path(registry_path+os.path.sep+to_lower(args.name)+os.path.sep+"controller").mkdir(parents=True, exist_ok=True)
        with open("registry_template/controller/SampleController.java.template", 'r') as f:
            content = f.read()
            content = content.replace("{{service_name_lower}}", to_lower(args.name))
            content = content.replace("{{service_name_pascal}}", to_pascal_case(args.name))
            content = content.replace("{{service_name_camel}}", to_camel_case(args.name))
        with open(registry_path+os.path.sep+to_lower(args.name)+os.path.sep+"controller"+os.path.sep+to_pascal_case(args.name)+"Controller.java", 'w') as f:
            f.write(content)
        
        '''Entity'''
        Path(registry_path+os.path.sep+to_lower(args.name)+os.path.sep+"entity").mkdir(parents=True, exist_ok=True)
        with open("registry_template/entity/SampleEntity.java.template", 'r') as f:
            content = f.read()
            content = content.replace("{{service_name_lower}}", to_lower(args.name))
            content = content.replace("{{service_name_pascal}}", to_pascal_case(args.name))
            content = content.replace("{{service_name_camel}}", to_camel_case(args.name))
        with open(registry_path+os.path.sep+to_lower(args.name)+os.path.sep+"entity"+os.path.sep+to_pascal_case(args.name)+"Entity.java", 'w') as f:
            f.write(content)

        '''Repository'''
        Path(registry_path+os.path.sep+to_lower(args.name)+os.path.sep+"repository").mkdir(parents=True, exist_ok=True)
        with open("registry_template/repository/SampleRepository.java.template", 'r') as f:
            content = f.read()
            content = content.replace("{{service_name_lower}}", to_lower(args.name))
            content = content.replace("{{service_name_pascal}}", to_pascal_case(args.name))
            content = content.replace("{{service_name_camel}}", to_camel_case(args.name))
        with open(registry_path+os.path.sep+to_lower(args.name)+os.path.sep+"repository"+os.path.sep+to_pascal_case(args.name)+"Repository.java", 'w') as f:
            f.write(content)
            
        '''Service'''
        Path(registry_path+os.path.sep+to_lower(args.name)+os.path.sep+"service"+os.path.sep+"impl").mkdir(parents=True, exist_ok=True)
        with open("registry_template/service/SampleService.java.template", 'r') as f:
            content = f.read()
            content = content.replace("{{service_name_lower}}", to_lower(args.name))
            content = content.replace("{{service_name_pascal}}", to_pascal_case(args.name))
            content = content.replace("{{service_name_camel}}", to_camel_case(args.name))
        with open(registry_path+os.path.sep+to_lower(args.name)+os.path.sep+"service"+os.path.sep+to_pascal_case(args.name)+"Service.java", 'w') as f:
            f.write(content)

        '''Service Impl'''
        with open("registry_template/service/impl/SampleServiceImpl.java.template", 'r') as f:
            content = f.read()
            content = content.replace("{{service_name_lower}}", to_lower(args.name))
            content = content.replace("{{service_name_pascal}}", to_pascal_case(args.name))
            content = content.replace("{{service_name_camel}}", to_camel_case(args.name))
            content = content.replace("{{service_name_upper}}", to_upper(args.name))
        with open(registry_path+os.path.sep+to_lower(args.name)+os.path.sep+"service"+os.path.sep+"impl"+os.path.sep+to_pascal_case(args.name)+"ServiceImpl.java", 'w') as f:
            f.write(content)
    

    '''Payload Validation json'''
    if Path(resourse_path+os.path.sep+"payloadValidation"+os.path.sep+to_camel_case(args.name)+"PayloadValidation.json").is_file() == False:
        payloadSchema = {
                "$schema": "http://json-schema.org/draft-07/schema#",
                "type": "object",
                "properties": {
                    f"{to_camel_case(args.name)}Id": {
                    "type": "string",
                    "description": f"description about {to_camel_case(args.name)}Id"
                    }
                },
                "required": [
                    f"{to_camel_case(args.name)}Id"
                ]
            }
        
        with open(resourse_path+os.path.sep+"payloadValidation"+os.path.sep+to_camel_case(args.name)+"PayloadValidation.json", "w") as f:
            json.dump(payloadSchema, f, indent=4)


    '''ES field mapping json'''
    if Path(resourse_path+os.path.sep+"EsFieldsmapping"+os.path.sep+"es"+to_pascal_case(args.name)+"RequiredFields.json").is_file() == False:
        esRequiredFields = {
            f"{to_camel_case(args.name)}Id": {
                "type": "keyword"
            }
        }        
        with open(resourse_path+os.path.sep+"EsFieldsmapping"+os.path.sep+"es"+to_pascal_case(args.name)+"RequiredFields.json", "w") as f:
            json.dump(esRequiredFields, f, indent=4)

       
    '''Constants variables'''
    with open(util_path+os.path.sep+"Constants.java", "r") as f:
        constants_content = f.read()
    
    if f"{to_upper(args.name)}_VALIDATION_FILE_JSON" in constants_content:
        print(f"Constants for '{to_camel_case(args.name)}' already exist, skipping.")
        return

    insertion_point = "    private Constants() {"
    if insertion_point not in constants_content:
        print("Could not find insertion point in Constants.java")
        return

    new_constants = f"""
    // {to_pascal_case(args.name)} Specific Constants
    public static final String {to_upper(args.name)}_VALIDATION_FILE_JSON = "/payloadValidation/{to_camel_case(args.name)}PayloadValidation.json";
    public static final String {to_upper(args.name)}_ID_RQST = "{to_camel_case(args.name)}Id";
    public static final String {to_upper(args.name)}_INDEX_NAME = "{to_camel_case(args.name)}_index";


    """
    updated_content = constants_content.replace(insertion_point, new_constants + insertion_point)

    with open(util_path+os.path.sep+"Constants.java", "w") as f:
        f.write(updated_content)

    '''Application properties'''
    with open(resourse_path+os.path.sep+"application.properties", "r") as f:
        application_properties = f.read() 

    if f"elastic.required.field.{to_camel_case(args.name)}.json.path" in application_properties:
        print(f"⚠️  elastic.required.field.{to_camel_case(args.name)}.json.path already exists, skipping.")
        return

    application_properties = application_properties + f"elastic.required.field.{to_camel_case(args.name)}.json.path = /EsFieldsmapping/es{to_pascal_case(args.name)}RequiredFields.json\n"
    
    with open(resourse_path+os.path.sep+"application.properties", "w") as f:
        f.write(application_properties)   


    '''Verg properties'''
    new_field = f"""
        @Value("${{elastic.required.field.{to_lower(args.name)}.json.path}}")
        private String elastic{to_pascal_case(args.name)}JsonPath;
    """
    with open(util_path+os.path.sep+"VergProperties.java", "r") as f:
        content = f.read()   

    if f"elastic{to_pascal_case(args.name)}JsonPath" in content:
        print(f"'elastic{to_pascal_case(args.name)}JsonPath' already exists, skipping.")
        return

    last_brace_index = content.rfind("}")
    updated_content  = content[:last_brace_index] + new_field + content[last_brace_index:]

    with open(util_path+os.path.sep+"VergProperties.java", "w") as f:
        f.write(updated_content)
    

    
if __name__ == '__main__':
    main()