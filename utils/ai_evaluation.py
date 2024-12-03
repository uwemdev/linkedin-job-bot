import yaml

def evaluate_job(job_description, resume_path='resume.yaml'):
    # Load the YAML resume
    with open(resume_path, 'r') as file:
        resume = yaml.safe_load(file)
    
    # Simple evaluation (to be expanded later with actual AI/ML logic)
    if 'developer' in job_description.lower() and 'python' in resume['skills']:
        return True
    return False