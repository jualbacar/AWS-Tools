# AWS-Tools

EC2-TAGS-CLONE

Script que copia los tags y sus valores de una instancia origen a una destino. El script debe utilizarse con profiles y requieres tener aws cli instalado.
Como output escupe los tags y el valor que se están escribiendo

```./ec2-tags-cloner.sh [profile] [id instancia origen] [id instancia destino]```

Ejemplo: ```./ec2-tags-cloner.sh serunion i-039d5bcd4554213b6 i-0a77b6800ce1c6aea```
