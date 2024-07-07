# Feature Store

See MLOps notes https://github.com/huang-pan/modern-data-stack-2023/blob/main/MLOps.md

## MLOps MVP: Feature Store + Model Registry
- Minimal / MVP MLOPs https://www.youtube.com/watch?v=nQR3fz1KD3g
![Screenshot_20240707-084619_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4e10bfd1-a979-49b5-8efa-f8d75f6829bb)
![Screenshot_20240707-084628_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/03d18282-9047-4748-899a-00b227a67ad2)
![Screenshot_20240707-084646_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0f469c04-cea1-4095-8c9a-90cc0834a48d)
![Screenshot_20240707-084650_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a73816dd-8d23-4d2f-9e8d-c8ea0b870fc0)
![Screenshot_20240707-084700_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5a9b2dc4-4e86-4f22-b4df-e9be3efc2cc2)
![Screenshot_20240707-084716_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cfd541cf-96c3-47dd-ab41-4d191d230753)
![Screenshot_20240707-084738_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9bb1ba2c-318c-4095-8466-68dd1dc20aa8)
![Screenshot_20240707-084749_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/83df0400-a9e2-4d1b-b658-febd6600e5a2)
![Screenshot_20240707-084814_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/77894788-6689-44e2-af9f-5cbba51dc0ee)
![Screenshot_20240707-084902_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/413141c2-d985-45c0-b738-87514712d192)
![Screenshot_20240707-084912_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cc9cd045-0e79-41e0-adc7-f3db6e2bdffd)
![Screenshot_20240707-084920_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/47adfb54-7a41-4069-af38-18906d6ed891)
![Screenshot_20240707-084931_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2588cc5a-1536-4fa4-949e-0ff71ab87434)
![Screenshot_20240707-084936_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8bed6a9a-c817-4a0c-bca2-9b8abe41ba51)
![Screenshot_20240707-084940_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/463b0af1-d5e9-45f3-afe1-e55c5316f36b)
![Screenshot_20240707-084949_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/71c71ebe-1b4f-4dc7-938a-2df239733194)
![Screenshot_20240707-084955_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/faacaeb3-28d4-4f93-83a0-db75e9f735a2)
![Screenshot_20240707-085027_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e16861b3-5af1-4559-9740-8b18ecf0c224)
![Screenshot_20240707-085033_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9d0a0546-bf83-46ef-8b97-7753a6d2da09)
![Screenshot_20240707-085121_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e5018d30-d844-4f11-b5a9-4a39e17aa66e)

## FeatureForm
- https://www.youtube.com/watch?v=ZsWa6XiBc-U
- Pulsar has retention layer: separates out historical part and puts it in S3, see https://www.youtube.com/watch?v=ZsWa6XiBc-U&t=170s
  - Confluent has retention layer, OSS Kafka does not
  - Kafka won event bus battle; Pulsar features are being pulled into Kafka
- batch features (OLAP / Databricks / Snowflake) + streaming features (Flink / RisingWave / Quix) like most popular DEXes used last 30 min (streaming analytics)
- offline / training feature store + online / inference feature store
- Most popular offline + online feature stores
  1. Databricks + redis
  2. Snowflake + redis
![Screenshot_20240703-182114_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/401c639c-034f-4cc0-9085-6ec29fa1eb1a)
![Screenshot_20240703-182124_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cef513a3-36cc-460b-808d-3bf2d569083a)
![Screenshot_20240703-182130_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f1b04f1b-b176-46ce-ab71-9010c746c771)
![Screenshot_20240703-182139_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8a27c4a0-a63e-451d-936b-1b6be42fceac)
![Screenshot_20240703-182205_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/de6850e9-3beb-4be1-a996-c35d0edca72a)
![Screenshot_20240703-182210_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5f5582de-61c7-4661-8823-0018240dbeda)
![Screenshot_20240703-182229_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b6a6bd33-478e-46f6-a5f1-339789817029)
![Screenshot_20240703-182237_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fca146ae-8e78-4a4d-bc80-4ef053126525)
![Screenshot_20240703-182243_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/66cdc4f4-781e-435e-a328-a938e0db75ec)
![Screenshot_20240703-182254_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7a9acf89-94dc-4b3e-a0d3-f6f2b1d10a23)
![Screenshot_20240703-182303_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b527b1ab-5d39-4f9e-ad2f-e351c481b721)
![Screenshot_20240703-182309_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/478fb190-bf81-46a2-8ccc-820fd40415f5)
![Screenshot_20240703-182326_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3da95fd7-e7b9-406c-821b-654fb78f4385)
![Screenshot_20240703-182332_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c8d2e88e-0776-4e3f-a88c-65c55df464f1)
![Screenshot_20240703-182401_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9271d6c2-2eb7-4360-a9e2-54ad6982e0bc)
![Screenshot_20240703-182403_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bd109228-ae75-4e6a-9b76-574670374511)
![Screenshot_20240703-182410_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/731283c7-19c9-4496-bb3b-dc22c0c1447c)
![Screenshot_20240703-182426_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/86144577-83ff-4f53-9e23-48bf1f6e4030)
![Screenshot_20240703-182429_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cd292f13-16c8-4439-837c-1c50f05214f4)
![Screenshot_20240703-182458_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8dca24e7-c156-464e-83aa-9944bf4d2777)
![Screenshot_20240703-182509_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/148a3ee0-9297-485d-a264-33fccb9e45ea)
![Screenshot_20240703-182513_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a7685566-0a52-4684-991e-ec2a55597b48)
![Screenshot_20240703-182517_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/afe71e93-104a-4cdb-927f-b5ad3bb7bdca)
![Screenshot_20240705-090456_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f38a89bd-b8ed-4e12-94ea-d0ebff66c7fb)
![Screenshot_20240703-182521_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6dd7e4a5-b143-48ce-8301-a6fdcbd3f6ed)
![Screenshot_20240705-090430_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6349a469-4e13-47d6-9677-b0b904a5d33d)
