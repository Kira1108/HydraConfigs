"""Since node.waldo is missing, you have to run the code with 
python app.py +node.waldo=111

You can both access configuation like a dictionary or like an object.
cfg.node.loompa == 10
cfg['node']['loompa'] == 10
"""


from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base = None, config_path = ".", config_name='config')
def my_app(cfg:DictConfig):
    assert cfg.node.loompa == 10
    assert cfg['node']['loompa'] == 10
    assert cfg.node.zippity == 10
    
    assert isinstance(cfg.node.zippity, int)
    assert cfg.node.do == "oompa 10"
    
    cfg.node.waldo
    
    print(OmegaConf.to_yaml(cfg))
    
    
if __name__ == "__main__":
    my_app()