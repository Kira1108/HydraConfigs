"""
Run the code with python app.py

Override config(without +sign):
python my_app.py db.user=root db.password=1234

Add a config which is not in config file
python my_app.py ++db.password=1234
"""

from omegaconf import OmegaConf, DictConfig
import hydra


@hydra.main(
    version_base = None, 
    config_path = '.', 
    config_name = "config")
def my_app(cfg):
    print(OmegaConf.to_yaml(cfg))
    
    
if __name__ == "__main__":
    my_app()