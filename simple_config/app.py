"""
Run the code with python my_app.py +db.driver=mysql +db.user=omry +db.password=secret

db:
  driver: mysql
  user: omry
  password: secret

"""


from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base = None)
def my_app(cfg:DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    
if __name__ == "__main__":
    my_app()

