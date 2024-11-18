![cover-v5-optimized](https://github.com/mlchain/mlchain/assets/13230914/f9e19af5-61ba-4119-b926-d10c4c06ebab)

<p align="center">
  📌 <a href="https://mlchain.khulnasoft.com/blog/introducing-mlchain-workflow-file-upload-a-demo-on-ai-podcast">Introducing Mlchain Workflow File Upload: Recreate Google NotebookLM Podcast</a>
</p>

<p align="center">
  <a href="https://cloud-mlchain.khulnasoft.com">Mlchain Cloud</a> ·
  <a href="https://docs-mlchain.khulnasoft.com/getting-started/install-self-hosted">Self-hosting</a> ·
  <a href="https://docs-mlchain.khulnasoft.com">Documentation</a> ·
  <a href="https://umlchain.app/chat/22L1zSxg6yW1cWQg">Enterprise inquiry</a>
</p>

<p align="center">
    <a href="https://mlchain.khulnasoft.com" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/Product-F04438"></a>
    <a href="https://mlchain.khulnasoft.com/pricing" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/free-pricing?logo=free&color=%20%23155EEF&label=pricing&labelColor=%20%23528bff"></a>
    <a href="https://discord.gg/FngNHpbcY7" target="_blank">
        <img src="https://img.shields.io/discord/1082486657678311454?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
            alt="chat on Discord"></a>
    <a href="https://reddit.com/r/mlchainai" target="_blank">  
        <img src="https://img.shields.io/reddit/subreddit-subscribers/mlchainai?style=plastic&logo=reddit&label=r%2Fmlchainai&labelColor=white"
            alt="join Reddit"></a>
    <a href="https://twitter.com/intent/follow?screen_name=mlchain_ai" target="_blank">
        <img src="https://img.shields.io/twitter/follow/mlchain_ai?logo=X&color=%20%23f5f5f5"
            alt="follow on X(Twitter)"></a>
    <a href="https://hub.docker.com/u/mlchain" target="_blank">
        <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/mlchain/mlchain-web?labelColor=%20%23FDB062&color=%20%23f79009"></a>
    <a href="https://github.com/mlchain/mlchain/graphs/commit-activity" target="_blank">
        <img alt="Commits last month" src="https://img.shields.io/github/commit-activity/m/mlchain/mlchain?labelColor=%20%2332b583&color=%20%2312b76a"></a>
    <a href="https://github.com/mlchain/mlchain/" target="_blank">
        <img alt="Issues closed" src="https://img.shields.io/github/issues-search?query=repo%3Amlchain%2Fmlchain%20is%3Aclosed&label=issues%20closed&labelColor=%20%237d89b0&color=%20%235d6b98"></a>
    <a href="https://github.com/mlchain/mlchain/discussions/" target="_blank">
        <img alt="Discussion posts" src="https://img.shields.io/github/discussions/mlchain/mlchain?labelColor=%20%239b8afb&color=%20%237a5af8"></a>
</p>

<p align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="./README_CN.md"><img alt="简体中文版自述文件" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
  <a href="./README_JA.md"><img alt="日本語のREADME" src="https://img.shields.io/badge/日本語-d9d9d9"></a>
  <a href="./README_ES.md"><img alt="README en Español" src="https://img.shields.io/badge/Español-d9d9d9"></a>
  <a href="./README_FR.md"><img alt="README en Français" src="https://img.shields.io/badge/Français-d9d9d9"></a>
  <a href="./README_KL.md"><img alt="README tlhIngan Hol" src="https://img.shields.io/badge/Klingon-d9d9d9"></a>
  <a href="./README_KR.md"><img alt="README in Korean" src="https://img.shields.io/badge/한국어-d9d9d9"></a>
  <a href="./README_AR.md"><img alt="README بالعربية" src="https://img.shields.io/badge/العربية-d9d9d9"></a>
  <a href="./README_TR.md"><img alt="Türkçe README" src="https://img.shields.io/badge/Türkçe-d9d9d9"></a>
  <a href="./README_VI.md"><img alt="README Tiếng Việt" src="https://img.shields.io/badge/Ti%E1%BA%BFng%20Vi%E1%BB%87t-d9d9d9"></a>
</p>


Mlchain is an open-source LLM app development platform. Its intuitive interface combines agentic AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. 

## Quick start
> Before installing Mlchain, make sure your machine meets the following minimum system requirements:
> 
>- CPU >= 2 Core
>- RAM >= 4 GiB

</br>

The easiest way to start the Mlchain server is through [docker compose](docker/docker-compose.yaml). Before running Mlchain with the following commands, make sure that [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) are installed on your machine:

```bash
cd mlchain
cd docker
cp .env.example .env
docker compose up -d
```

After running, you can access the Mlchain dashboard in your browser at [http://localhost/install](http://localhost/install) and start the initialization process.

#### Seeking help
Please refer to our [FAQ](https://docs-mlchain.khulnasoft.com/getting-started/install-self-hosted/faqs) if you encounter problems setting up Mlchain. Reach out to [the community and us](#community--contact) if you are still having issues.

> If you'd like to contribute to Mlchain or do additional development, refer to our [guide to deploying from source code](https://docs-mlchain.khulnasoft.com/getting-started/install-self-hosted/local-source-code)

## Key features
**1. Workflow**: 
  Build and test powerful AI workflows on a visual canvas, leveraging all the following features and beyond.


  https://github.com/mlchain/mlchain/assets/13230914/356df23e-1604-483d-80a6-9517ece318aa



**2. Comprehensive model support**: 
  Seamless integration with hundreds of proprietary / open-source LLMs from dozens of inference providers and self-hosted solutions, covering GPT, Mistral, Llama3, and any OpenAI API-compatible models. A full list of supported model providers can be found [here](https://docs-mlchain.khulnasoft.com/getting-started/readme/model-providers).

![providers-v5](https://github.com/mlchain/mlchain/assets/13230914/5a17bdbe-097a-4100-8363-40255b70f6e3)


**3. Prompt IDE**: 
  Intuitive interface for crafting prompts, comparing model performance, and adding additional features such as text-to-speech to a chat-based app. 

**4. RAG Pipeline**: 
  Extensive RAG capabilities that cover everything from document ingestion to retrieval, with out-of-box support for text extraction from PDFs, PPTs, and other common document formats.

**5. Agent capabilities**: 
  You can define agents based on LLM Function Calling or ReAct, and add pre-built or custom tools for the agent. Mlchain provides 50+ built-in tools for AI agents, such as Google Search, DALL·E, Stable Diffusion and WolframAlpha.

**6. LLMOps**: 
  Monitor and analyze application logs and performance over time. You could continuously improve prompts, datasets, and models based on production data and annotations.

**7. Backend-as-a-Service**: 
  All of Mlchain's offerings come with corresponding APIs, so you could effortlessly integrate Mlchain into your own business logic.


## Using Mlchain

- **Cloud </br>**
We host a [Mlchain Cloud](https://mlchain.khulnasoft.com) service for anyone to try with zero setup. It provides all the capabilities of the self-deployed version, and includes 200 free GPT-4 calls in the sandbox plan.

- **Self-hosting Mlchain Community Edition</br>**
Quickly get Mlchain running in your environment with this [starter guide](#quick-start).
Use our [documentation](https://docs-mlchain.khulnasoft.com) for further references and more in-depth instructions.

- **Mlchain for enterprise / organizations</br>**
We provide additional enterprise-centric features. [Log your questions for us through this chatbot](https://umlchain.app/chat/22L1zSxg6yW1cWQg) or [send us an email](mailto:business@mlchain.khulnasoft.com?subject=[GitHub]Business%20License%20Inquiry) to discuss enterprise needs. </br>
  > For startups and small businesses using AWS, check out [Mlchain Premium on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-t22mebxzwjhu6) and deploy it to your own AWS VPC with one-click. It's an affordable AMI offering with the option to create apps with custom logo and branding.


## Staying ahead

Star Mlchain on GitHub and be instantly notified of new releases.

![star-us](https://github.com/mlchain/mlchain/assets/13230914/b823edc1-6388-4e25-ad45-2f6b187adbb4)


## Advanced Setup

If you need to customize the configuration, please refer to the comments in our [.env.example](docker/.env.example) file and update the corresponding values in your `.env` file. Additionally, you might need to make adjustments to the `docker-compose.yaml` file itself, such as changing image versions, port mappings, or volume mounts, based on your specific deployment environment and requirements. After making any changes, please re-run `docker-compose up -d`. You can find the full list of available environment variables [here](https://docs-mlchain.khulnasoft.com/getting-started/install-self-hosted/environments).

If you'd like to configure a highly-available setup, there are community-contributed [Helm Charts](https://helm.sh/) and YAML files which allow Mlchain to be deployed on Kubernetes.

- [Helm Chart by @LeoQuote](https://github.com/douban/charts/tree/master/charts/mlchain)
- [Helm Chart](https://github.com/MLChain/mlchain-helm)
- [YAML file](https://github.com/MLChain/mlchain-kubernetes)

#### Using Terraform for Deployment

Deploy Mlchain to Cloud Platform with a single click using [terraform](https://www.terraform.io/)

##### Azure Global
- [Azure Terraform](https://github.com/MLChain/mlchain-azure-terraform)

##### Google Cloud
- [Google Cloud Terraform by @sotazum](https://github.com/DeNA/mlchain-google-cloud-terraform)

## Contributing

For those who'd like to contribute code, see our [Contribution Guide](https://github.com/mlchain/mlchain/blob/main/CONTRIBUTING.md). 
At the same time, please consider supporting Mlchain by sharing it on social media and at events and conferences.


> We are looking for contributors to help with translating Mlchain to languages other than Mandarin or English. If you are interested in helping, please see the [i18n README](https://github.com/mlchain/mlchain/blob/main/web/i18n/README.md) for more information, and leave us a comment in the `global-users` channel of our [Discord Community Server](https://discord.gg/8Tpq4AcN9c).

## Community & contact

* [Github Discussion](https://github.com/mlchain/mlchain/discussions). Best for: sharing feedback and asking questions.
* [GitHub Issues](https://github.com/mlchain/mlchain/issues). Best for: bugs you encounter using MlChain, and feature proposals. See our [Contribution Guide](https://github.com/mlchain/mlchain/blob/main/CONTRIBUTING.md).
* [Discord](https://discord.gg/FngNHpbcY7). Best for: sharing your applications and hanging out with the community.
* [X(Twitter)](https://twitter.com/mlchain_ai). Best for: sharing your applications and hanging out with the community.

**Contributors**

<a href="https://github.com/mlchain/mlchain/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mlchain/mlchain" />
</a>

## Star history

[![Star History Chart](https://api.star-history.com/svg?repos=mlchain/mlchain&type=Date)](https://star-history.com/#mlchain/mlchain&Date)


## Security disclosure

To protect your privacy, please avoid posting security issues on GitHub. Instead, send your questions to security@mlchain.khulnasoft.com and we will provide you with a more detailed answer.

## License

This repository is available under the [Mlchain Open Source License](LICENSE), which is essentially Apache 2.0 with a few additional restrictions.

