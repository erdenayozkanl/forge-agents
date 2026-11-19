import argparse
import json
from agents.workflow import Workflow

def main():
    p=argparse.ArgumentParser(description='ForgeAgents: auditable bounded multi-step research workflow')
    p.add_argument('task',nargs='?',default='Explain how to evaluate hybrid retrieval')
    p.add_argument('--ollama',action='store_true',help='Use a local Ollama model for report writing')
    p.add_argument('--serve',action='store_true')
    args=p.parse_args()
    if args.serve:
        import uvicorn
        uvicorn.run('api:app',host='127.0.0.1',port=8002)
    else:
        print(json.dumps(Workflow(llm=args.ollama).run(args.task),indent=2))
if __name__=='__main__':main()
