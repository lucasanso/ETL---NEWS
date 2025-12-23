import scrapy
import yaml
import os




CHECKPOINT_FILE = 'checkpoints.yaml' # arquivo para guardar as palavras-chave que já foram percorridas.


class EstadaoSpider(scrapy.spider):
    name = "estadao_crawler"
    allowed_domains = ["estadao.com.br"]
    
    # Compreender o funcionamento do Playwright primeiro para depois implementar aqui
    custom_settings = {
    
    def carregar_checkpoint(self):
        # Caso em que o arquivo ainda não foi criado:
        
        if not os.path.exists(CHECKPOINT_FILE):
            return []
        
        try:
            with open(CHECKPOINT_FILE, 'r') as arq:
                data = yaml.safe_load(arq)
                if data and 'palavras_finalizadas' in data:
                    return data['palavras_finalizadas']
        
        except Exception as e:
            print(f'Erro ao ler arquivo de checkpoint {e}')
        
        return []
        
        
    def salvar_checkpoint(self, keyword):
        completas = self.carregar_checkpoint()
        
        if keyword not in completas:
            completas.append(keyword)
            
            try:
                with open(CHECKPOINT_FILE, 'r') as f:
                    yaml.dump({'palavras_finalizadas' : completas}, f) # salvando os dados no yaml
            except Exception as e:
                self.logger.error(f"Erro ao salvar palavra-chave no arquivo checkpoint: {e}")
            
    
    
    
    
    
    
    
    }
