# Neuro-Symbolic AI Tutorial for Industry 4.0

Welcome to the [NeSyAI4 Tutorial for Industry 4.0](https://sites.google.com/view/nesyai4-2023/home) Repository at the International Semantic Web Conference!

This repository serves as a resource for attendees of our hands-on tutorial on Neuro-Symbolic AI for Industry 4.0. In this tutorial, we explore the fusion of semantic web technology and machine learning, demonstrating practical applications in the context of Industry 4.0.

During the hands-on session at the International Semantic Web Conference, participants will gain practical experience in applying Neuro-Symbolic AI to Industry 4.0. They'll explore semantic technology, ontologies, and deep learning to address real-world manufacturing challenges, using Bosch scenarios as examples.

## Organizers

This tutorial is organized field of Neuro-Symbolic AI and Industry 4.0:

- **[Diego Rincon-Yanez](https://d1egoprog.co)**  
  *Affiliation:* Bosch Center for AI 
  *Email:* fixed-term.diego.rincon \[at\] de.bosch.com, rinconyanezd+iswc \[at\] gmail.com 

- **[Irlan Grangel-Gonzalez](https://www.linkedin.com/in/dr-irlan-grangel-gonzalez/)**    
  *Affiliation:* Bosch Corporate Research
  *Email:* irlan.grangelgonzalez \[at\] de.bosch.com

- **[Mohamed H. Gad-elrab](https://www.linkedin.com/in/gadelrab/)**    
  *Affiliation:* Bosch Corporate Research
  *Email:* Mohamed.Gad-Elrab \[at\]  de.bosch.com

- **[Yuqicheng Zhu](https://www.linkedin.com/in/yuqicheng-zhu-531658161/)**
  *Affiliation:* Bosch Center for AI
  *Email:* Yuqicheng.Zhu \[at\] de.bosch.com

- **[Evgeny Kharlamov](https://www.linkedin.com/in/evgeny-kharlamov-98721a7/)**    
  *Affiliation:* Bosch Corporate Research
  *Email:* Evgeny.Kharlamov \[at\]  de.bosch.com

Feel free to reach out to us with any questions or concerns regarding the tutorial. We look forward to your participation!

## Requirements

Make sure you have the following installed software before starting the hands-on session:

- Git Client
- Text Editor
- Docker Engine Instance

## Running the example using docker compose

Download the prepared `compose.yaml` file from the repository via `wget` and execute the command using the utility.

``` BASH
git clone https://github.com/d1egoprog/ISWC23-I40Tutorial.git
docker compose -p ISWC23-i40 up -d
```

The previous lines will download the repository (specially for the example files) and run the following docker compose file automatically in a pipeline fashion.

``` YAML
version: '3.7'

services:
  mapping:
    build: 
      context: ./1.${COMPONENT_1}/.
      args:
        - VERSION=${VERSION}
        - COMPONENT_NAME=${COMPONENT_1}
    environment:
      - ONTOLOGY=${ONTOLOGY}
      - OUTPUT_KG=${OUTPUT_KG}
      - INPUT_MAPPING=${INPUT_MAPPING}
    volumes:
      - ./files/datasources:/opt/${COMPONENT_1}/datasources
      - ./files/ontologies:/opt/${COMPONENT_1}/ontologies
      - ./files/mappings:/opt/${COMPONENT_1}/mappings
      - ./files/output:/opt/${COMPONENT_1}/output
    image: ${PROJECT_PREFIX}-${COMPONENT_1}:${VERSION}
  querying:
    environment:
      - INPUT_KG=${OUTPUT_KG}_merged.ttl
    volumes:
    - ./files/output:/opt/jena-fuseki/output
    - ./files/logs:/opt/jena-fuseki/logs
    ports:
      - 3030:3030
    image: d1egoprog/jena-fuseki:4.9.0-web
    depends_on:
      mapping:
        condition: service_completed_successfully
  visualization:
    image: d1egoprog/webvowl:1.1.7
    ports:
        - 8080:8080
    restart: always
    depends_on:
      mapping:
        condition: service_completed_successfully
```

## Feedback and Contributions:

We welcome your feedback and contributions to this repository. If you have suggestions, improvements, or additional resources to share, please feel free to open issues, submit pull requests, or reach out to the tutorial organizers.

Enjoy your learning journey with Neuro-Symbolic AI for Industry 4.0!
