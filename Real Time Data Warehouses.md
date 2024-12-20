# Real Time Data Warehouses

## RocksDB / Rockset
- Rockset is dead 2024, bought buy OpenAI, not supporting services anymore
	- https://www.linkedin.com/posts/rdmeyersf_druid-pinot-activity-7214310215423275009-BquL/
- Rockset replicates AWS DynamoDB tables https://www.youtube.com/watch?v=JGIzdFHZVXs
	- Rockset search and analytics DB https://www.youtube.com/watch?v=xGaUJTHuehQ
 	- Essentially makes a low latency copy of data source using 
		- converged indicies: row based index, column based index, inverted (document) index
- Rockset product overview https://www.youtube.com/watch?v=4nEQpISidw4
![Screenshot_20240620-104355_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0baab291-2d40-4db4-9efc-8ed3b2820df8)
- Rockset architecture https://www.youtube.com/watch?v=msW8nh5TTwQ
![Screenshot_20240620-115528_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8cd2eb60-95ca-4e0d-950d-0bd92ec6f27d)
![Screenshot_20240620-115550_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4cb73583-4b99-475a-9efe-c48a65875721)
- Snowflake export to S3 import to Rockset https://www.youtube.com/watch?v=siAqYzlcEiU

## Pinot vs Druid vs ClickHouse
- Real Time OLAP data warehouses by Pinot / StarTree https://www.youtube.com/watch?v=rJvDQSjmZCg
	- only Pinot supports Delta Lake / Snowflake / BigQuery as a data source
 	- Pinot supports a lot more index types
  	- All 3 (Pinot, Druid, ClickHouse) are bad at multi-table joins
  	- ClickHouse has best support for BI tools
![Screenshot_20240621-162116_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6e22630c-58b7-4e2a-a8a8-27c0506d7625)
![Screenshot_20240621-162131_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b9728ef6-9535-4819-aebb-bc923d0d3924)
![Screenshot_20240621-162140_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e0cfad74-3df4-49d0-aab0-2f44442d0db0)
![Screenshot_20240621-162203_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/11391135-e222-4f01-8989-6d18460e3eee)
![Screenshot_20240621-162219_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bf765599-246a-4291-b9be-b5ff921e35d1)
![Screenshot_20240621-162230_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d8108f17-37a1-435b-842b-aea27228f7b3)
![Screenshot_20240621-162239_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a5fbbef6-a1d6-43fb-856d-9ac70585653e)
![Screenshot_20240621-162302_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c037ea26-44d5-4090-a8e0-7bd37b589fc9)
![Screenshot_20240621-162306_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6e69f0eb-84b5-48e5-b1ff-aa34d248acbd)
![Screenshot_20240621-162320_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/39fcc694-a343-44a5-9b73-9a30e11ded7c)
![Screenshot_20240621-162333_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c4b0107b-ba80-498d-b0d7-e4a1eac967d5)
![Screenshot_20240621-162338_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bc629e87-7911-4c20-9bb2-5cf2803bb3c8)
![Screenshot_20240621-162342_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bde2a468-bd17-4633-8b7e-5a62daa3d206)
![Screenshot_20240621-162346_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5776f9d3-e105-4505-88c7-838c0aeba1fd)
![Screenshot_20240621-162349_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c5dd374e-e948-42c8-b6ae-868ab2daa7a2)
![Screenshot_20240621-162358_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/361cfc38-65ee-458c-96dc-03c0cbd876e1)
![Screenshot_20240621-162405_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cb0dd973-8ab9-47bd-aaf4-dc6803f585a4)
![Screenshot_20240621-162416_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9556cff3-45ba-419c-8dda-71ed9093ff06)
![Screenshot_20240621-162425_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f59cebf4-e4b0-45fd-b5b8-71cb44403bf2)
![Screenshot_20240621-162428_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9af007e0-5390-4084-aba2-8c9112cee01e)
![Screenshot_20240621-162436_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ca657532-f536-4b41-a89d-c1339a2cd40d)
![Screenshot_20240621-162440_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9c37cae1-05bc-4b8a-b014-e7ceab54153e)
![Screenshot_20240621-162444_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2a7f091a-15b2-4af5-b1ec-d99add6fb800)
![Screenshot_20240621-162454_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fa1e401d-e954-4d5f-bad5-02ee4d03c5b2)
![Screenshot_20240621-162506_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9ab45cff-870e-4469-a204-194c5be33708)
![Screenshot_20240621-162510_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9991f810-ae90-46bc-812c-d2a3cb719ce5)
![Screenshot_20240621-162526_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bf22ff49-fa2e-473a-88c0-ac35a69861f9)
![Screenshot_20240621-162543_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fe8c991c-507e-4328-a5e4-b66e21fe1056)
![Screenshot_20240621-162547_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7731e952-9702-4350-b467-e383be9e08bf)
![Screenshot_20240621-162557_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a385fa14-fd14-4594-9717-bd8a96fb40bb)
![Screenshot_20240621-162609_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9aba5cc3-3f5c-41ab-8f30-f2e1da348f4d)
![Screenshot_20240621-162612_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/691b1521-3838-47c5-9ac6-f06591a4530c)
![Screenshot_20240621-162619_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a903c1c8-57d5-419d-bb74-b394dc6b3f5c)
![Screenshot_20240621-162631_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c8abf184-4f08-4eff-aefb-ddc8911d7d1c)
![Screenshot_20240621-162638_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e1d9f3bb-3f7a-43fb-b34b-5f88a36273a0)
![Screenshot_20240621-162644_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/986de999-c31d-42d9-917e-35cc65c3ce91)
![Screenshot_20240621-162649_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dadb4026-f138-4079-818f-41d95e69fe88)
![Screenshot_20240621-162657_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2deea5f4-a689-4387-af62-455b4766734a)
![Screenshot_20240621-162703_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e6d496fa-9dc1-449e-b1d9-66cf43cf5860)
![Screenshot_20240621-162709_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9fdccf86-b106-4dd8-8170-6f158ffda831)
![Screenshot_20240621-162715_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/216e52c7-67d6-4f87-bdc4-a27c4b01098d)
![Screenshot_20240621-162727_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8eeecc88-70d5-4602-98d6-3456ac8cf1bd)

## Druid / Imply
- Druid older technology trying to modernize https://www.youtube.com/watch?v=4qP_z8n8in0
![Screenshot_20240620-171956_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/71cf93e8-739b-4174-95bc-dced43b3a9d7)
![Screenshot_20240620-171959_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/96560803-433d-4ae7-b84b-79fc60e629fa)
- Druid still behind? https://www.youtube.com/watch?v=wgJaB_PuHO4
![Screenshot_20240620-172640_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f9fdf6f9-c52c-49ce-96ab-4e12d746a737)
![Screenshot_20240620-172748_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b17ce331-2bf3-4410-8210-d42c5895fa17)
![Screenshot_20240620-172802_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8e4202ff-0842-491b-b7ba-212ee5e06692)
![Screenshot_20240620-172822_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dc153468-9aa2-4463-9ea2-7d148a60ac6e)
![Screenshot_20240620-172828_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/591fac46-6e5f-477c-b9f3-5915dd4efa3b)

## Pinot / StarTree
- Intro to Pinot https://www.youtube.com/live/AEuWx7yX6xw
![Screenshot_20240701-145423_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8c2370d0-e712-4242-ba9e-aad608468000)
![Screenshot_20240701-145444_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f715b92d-b81b-40eb-af5b-f804b6aec181)
![Screenshot_20240701-145449_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bd8faf97-2825-4042-a2ba-394290609473)
![Screenshot_20240701-145452_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b95d7947-b7c9-463b-afa3-49db746ea5de)
![Screenshot_20240701-145457_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8626dcc6-0995-422c-8dc0-e3807759ce47)
![Screenshot_20240701-145510_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ab1e4a0f-a833-4c63-b38b-17e656c50e76)
![Screenshot_20240701-145520_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/229b0605-5491-4000-afd4-c79999c4551b)
![Screenshot_20240701-145535_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dcdbcbaa-61fc-47e1-80f9-55672b92cd83)
![Screenshot_20240701-145547_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/719666d8-4f0a-4e89-95a2-35394cdbec87)
- Apache Pinot / StarTree https://www.youtube.com/watch?v=F8Q_pGIH9yY
![Screenshot_20240621-154808_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9f6455ba-3cc2-43e7-83b1-2df50b8cd8fb)
![Screenshot_20240621-154846_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/41e06c92-dd6e-4c9a-8766-625afb81f6f9)
![Screenshot_20240621-154933_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/329182ec-36d2-4cf0-911d-c1aa0d0ff7b8)
![Screenshot_20240621-155015_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/df5088db-dd69-4599-993e-ae92703ca0d2)
![Screenshot_20240621-155033_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ea8332dd-ef3c-47c3-8f61-bf1c8f6b2bd6)
![Screenshot_20240621-155058_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4b6917b4-aaf4-4e0d-9a2d-9685998beb41)
![Screenshot_20240621-155135_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5a45f2c8-53b4-4d45-866c-0044ac86705f)
![Screenshot_20240621-155156_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/749f6d0c-bfa6-4b95-90f0-fecf996c2ac3)
![Screenshot_20240621-155200_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/385c51ba-d55e-4dfe-bd05-7e88576e391f)
![Screenshot_20240621-155215_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ffa98b6d-77d4-4fb1-9b9a-33ed280e62ec)
- Star-Tree Index: Space-Time Trade Off in OLAP https://www.youtube.com/watch?v=bwO0HSXguFA
![Screenshot_20240703-173623_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/08563aa8-4c1f-4df6-b0b4-6c99b87485ca)
![Screenshot_20240703-173645_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5fa37e29-f131-4181-bd7d-f616066cc86b)
![Screenshot_20240703-173650_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3ad848b2-71be-466b-ad65-c80a7ea763dd)
![Screenshot_20240703-173657_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/35c88fb5-a7bf-4c78-892c-972de7ce77c6)
![Screenshot_20240703-173704_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9ab2cc12-e97f-415b-8f28-16bf57319c34)
![Screenshot_20240703-173715_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5cb62693-a80c-428b-8ecb-622a5238dae8)
![Screenshot_20240703-173732_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7c5bcfd0-af28-46c8-ac1e-09f44fc8f655)
![Screenshot_20240703-173735_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8102dec2-c36d-4e46-8a11-7e1fdb00f67b)
![Screenshot_20240703-173743_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6de73306-bdf9-4378-ab38-276b6d6ccfe4)
![Screenshot_20240703-173748_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/927eef21-71d1-481e-9678-8f9a7769ea38)
![Screenshot_20240703-173752_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ee4dfa3f-6d9f-45ed-8fa7-1321c98e22c4)
![Screenshot_20240703-173801_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/75b553aa-6b7d-47ae-865d-7f8a2d436cc6)
![Screenshot_20240703-173810_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b957516f-d035-4ecc-ad04-6392dda6572c)
![Screenshot_20240703-173812_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3f6537db-2b41-49ac-85fb-983e88d914d3)
![Screenshot_20240703-173825_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0eca5aa4-ff02-4468-a4a0-3cdc5e8aaa77)
![Screenshot_20240703-173832_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/532c8b43-25da-4e2d-9edf-15d5b0206c99)
![Screenshot_20240703-173836_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3b0bd2a0-5e17-4752-9bcd-e075dbcae40d)
![Screenshot_20240703-173845_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/50310789-5011-41cb-b82b-af81e5933906)
![Screenshot_20240703-173851_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4ea39dec-10d4-4ba4-ace3-a590d0577bc6)
![Screenshot_20240703-173902_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3241de6f-6c56-4a22-920f-0fcfbe8a108e)
![Screenshot_20240703-173910_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0a93ad3d-ccf7-47d4-84d6-6888625c341b)
![Screenshot_20240703-173924_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/28a85884-d739-4cc0-a93b-a04173579ca3)
![Screenshot_20240703-173938_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2648cbf9-c4b9-4404-b510-500c4b5f0cba)
![Screenshot_20240703-173948_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1ad65df6-6f4c-45da-b3c6-1080315417cc)
![Screenshot_20240703-173957_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/106dfd92-f922-47a8-b579-5e8c9127f746)
- Pinot Architecture https://www.youtube.com/watch?v=vYjef-KTuzY
![Screenshot_20240621-155801_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f40d6d17-02dc-40ae-a655-8a7458002f44)
![Screenshot_20240621-155819_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b2feab2c-c98f-4fcd-a186-703643a443b9)
![Screenshot_20240621-155828_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/13d14dd9-8dae-4c93-a54e-e4b57d9c41d2)
![Screenshot_20240621-155902_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e46f463d-957d-4916-858a-44dd28a4ea8e)
![Screenshot_20240621-155942_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e619b096-e1fc-4933-92ea-1e33c4922e6e)
![Screenshot_20240621-155950_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1b080d9b-3193-4799-a4b6-df7978d0187c)
![Screenshot_20240621-160014_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5b4e5974-c484-488f-9497-38a181e61899)
![Screenshot_20240621-160045_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ee7c466f-9d20-4ec7-9ae2-77b006d10cf0)
![Screenshot_20240621-160120_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8bc779ec-063f-47b1-af53-df8dc9bf5a0a)
![Screenshot_20240621-160129_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/99a30dd5-5c8f-49d7-87c3-8d19aa410cc7)
![Screenshot_20240621-160142_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2caae1f0-2efe-4851-a062-932e8ec1053e)
![Screenshot_20240621-160239_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/12e990b3-342f-481a-928d-ccb15b40a12e)
![Screenshot_20240621-160249_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/594bc3bf-33ec-4946-bd22-23268571b7ab)
![Screenshot_20240621-160304_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8da8cdbd-6ae0-4fbf-8bb4-2f05126e5f52)
![Screenshot_20240621-160310_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5b862b8c-b05b-43ba-b84c-b8e281c84010)
![Screenshot_20240621-160324_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/75ec2692-1ca2-4591-ad5d-261eeae76100)
![Screenshot_20240621-160330_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fdcb3292-5394-47b5-8b5e-3be1dff966d8)
![Screenshot_20240621-160344_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/39579a85-e325-431f-97b0-bf711f133bcf)
![Screenshot_20240621-160355_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1042384d-78ce-42ed-8a1e-ae7115dfb52e)
![Screenshot_20240621-160412_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9fa1aa9c-1dc1-4a63-a80d-2702d45968c1)
![Screenshot_20240621-160438_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/13749ca6-eba0-4b35-ada9-4f46f8785be3)
![Screenshot_20240621-160448_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6a577648-3f9b-4f67-916e-be290050ef57)
![Screenshot_20240621-160455_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3c095ba3-3f58-41ea-be16-7148f12bb4db)
![Screenshot_20240621-160515_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/43c9df67-a599-414b-ba12-9abb48ed3be0)

## ClickHouse
- ClickHouse
	- https://www.youtube.com/watch?v=HRh5setqGCU
 	- https://www.youtube.com/watch?v=cwJsjHDLE8I
	- RT data warehouse
		- internet scale event data, very fast aggregations, very resource efficient, less expensive
		- low latency 100 ms, high concurrency
	- main use cases
		- fraud detection, eccommerce
		- sentiment analysis
		- sales and marketing analytics
		- customer usage data, billing usage data
		- low latency, high concurrency: B2B SaaS 1/3
		- cloud DW: perf, cheaper than Snowflake 1/3
		- observability, logging, tracing, metrics, Elasticsearch Logstash Kibana 1/3
- ClickHouse bad at joins https://www.youtube.com/watch?v=1xvFZskEp1o
	- StarRocks good at RT joins, cost based query optimizer
	- Clickhouse bad at RT joins, good for RT log search, rule based query optimizer 
![Screenshot_20240620-155335_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/baf6af95-fdfd-4909-8f9b-5fd6f9c3572a)
![Screenshot_20240620-155342_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c4d87720-36bc-49e5-a9c4-6cd85cc54be7)
![Screenshot_20240620-155351_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8965b522-2ba9-487a-a273-6864213f5f2c)
![Screenshot_20240620-155356_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7771ba48-da75-4d40-b1c5-5def7789415f)
![Screenshot_20240620-155416_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fca6e407-4baa-474e-8c39-fb62758817db)
![Screenshot_20240620-155430_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/537cbbdc-6716-4cbf-a610-cf9ce1dd14c5)
![Screenshot_20240620-155436_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dc05c366-0596-43ce-aba7-de67d3fc2c85)
![Screenshot_20240620-155442_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a7fb417f-ccc1-48e5-a54d-0d7be3626d6f)
![Screenshot_20240620-155445_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3ddd6b93-d4ec-4d7c-87f9-3978e576cefc)
![Screenshot_20240620-155452_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/009ec7d5-3dc6-4b48-8165-28e50f59a4a1)
![Screenshot_20240620-155458_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/aadee248-e9f3-4c56-b0e9-81ec02ebd4b2)
![Screenshot_20240620-155504_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/00ea382d-1179-4e97-87ab-300d8a414740)
![Screenshot_20240620-155520_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a20840f0-5c45-4b3d-9e14-b124e968a4d4)
![Screenshot_20240620-155523_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/278a91f6-cb24-4a31-bee5-03cf48ccc975)
- ClickHouse: Powering Coinhall's Real Time Blockchain Data Platform https://www.youtube.com/watch?v=za59qlT54T8
![Screenshot_20240729-093846_YouTube](https://github.com/user-attachments/assets/cab87308-9f9e-4fae-9958-b011a2664f7c)
![Screenshot_20240729-093857_YouTube](https://github.com/user-attachments/assets/e2f2158d-9f54-4a9f-bcf4-5d4b4e3e6be0)
![Screenshot_20240729-094010_YouTube](https://github.com/user-attachments/assets/2ab5a278-c237-4a04-a121-01111c37ea00)
![Screenshot_20240729-094031_YouTube](https://github.com/user-attachments/assets/ec135fa2-f775-4937-b0d2-7cd9569bf127)
![Screenshot_20240729-094205_YouTube](https://github.com/user-attachments/assets/65e3069f-ef1a-4c72-9886-0aa6b008edd9)
![Screenshot_20240729-094335_YouTube](https://github.com/user-attachments/assets/75f1f291-516e-4705-b3ee-43db4c809218)
![Screenshot_20240729-094341_YouTube](https://github.com/user-attachments/assets/0fec4748-e616-4e43-bf16-e7fd689a2380)
![Screenshot_20240729-094355_YouTube](https://github.com/user-attachments/assets/d5fa63f4-e0d0-44ee-952c-9292dc4ba45a)
![Screenshot_20240729-094400_YouTube](https://github.com/user-attachments/assets/21993795-e889-4d43-b03c-b0db5425fa42)

## Firebolt
- https://www.firebolt.io/resources/data-warehouse-comparison-guide
	- Firebolt vs Snowflake vs Athena vs Redshift vs Druid https://www.youtube.com/watch?v=njXKSlVZGAY
- Firebolt is a modified ClickHouse https://www.youtube.com/watch?v=9rW9uEJ15tU
![Screenshot_20240703-180051_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ee42df08-8ecf-4568-9b84-3cb29c9be67a)
![Screenshot_20240703-180109_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cd511669-cec3-499b-b128-116ad0708ff3)
![Screenshot_20240703-180121_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3e4db3b8-940a-4e09-a49c-5e8769bd631c)
![Screenshot_20240703-180131_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e8b0ce44-d4f2-4619-9837-7f5410db4292)
![Screenshot_20240703-180146_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ae7b8d72-a28d-48d8-b34d-a3777295297d)
![Screenshot_20240703-180149_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1fd7b3d0-5778-4e48-90be-595b4e082716)
![Screenshot_20240703-180155_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b49f1236-e27e-4cc0-a20b-c847899e9475)
![Screenshot_20240703-180228_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/749a8001-473e-4ed0-9ea1-a50e852970f6)
![Screenshot_20240703-180242_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2fe2ed46-b5ff-4069-8d02-22d68c6b09b4)
![Screenshot_20240703-180251_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/821ee14d-a4b5-4375-b1f5-17f46350be38)
![Screenshot_20240703-180302_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/85b614e1-84f1-4325-92f0-e272054b02d7)
![Screenshot_20240703-180309_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/df8878a8-d7b3-4c92-badb-9255ad995d2e)
![Screenshot_20240703-180317_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/961168b9-919c-44a3-8070-bd65a52b6c94)
![Screenshot_20240703-180336_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bfad1afe-81ec-4f81-9a1e-14a18dae760c)
![Screenshot_20240703-180350_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7a0e9708-c117-4d01-b7ea-71cc94456295)
![Screenshot_20240703-180356_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8837a7be-379b-43cf-bec2-ee6582173953)
![Screenshot_20240703-180406_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/727c27fc-eb0b-4f73-b2d4-40a9586458b8)
- Firebolt fastest RT cloud data warehouse https://www.youtube.com/watch?v=K0g4GUY7PMI
	- faster, cheaper than Snowflake
![Screenshot_20240620-161328_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fbb56250-63ea-48aa-b449-d13ae8343f98)
![Screenshot_20240620-161346_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/269536c7-b5dd-4f50-9236-cd94df745cd1)
![Screenshot_20240620-161358_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fa1d4102-a007-4976-812e-61140c134dd1)
![Screenshot_20240620-161419_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8ce84079-ebb6-420e-bed2-5081e2ac6874)
![Screenshot_20240620-161434_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ed1c63ae-02d7-4a19-b956-ad3da2026de2)

## Materialize
- Intro to Materialize https://www.youtube.com/watch?v=Ahu8C-oh7A4
![Screenshot_20240703-060931_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/81f55692-fcd0-4a5f-8731-92d21edc4c89)
![Screenshot_20240703-060946_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3d8cf225-f1a7-424e-84ae-0d8d5492de7c)
![Screenshot_20240703-060955_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bd8666d1-c154-4af4-9de1-64ee2c40a019)
![Screenshot_20240703-061010_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1eeb4318-fe76-47d7-9473-954730d9b242)
![Screenshot_20240703-061018_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f812aee3-aa01-41bc-8f62-488d7e351e57)
![Screenshot_20240703-061023_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c4acd98a-f759-4167-8de6-7285063a5bde)
![Screenshot_20240703-061029_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/efcd8210-6496-4fff-9179-267408418f4f)
![Screenshot_20240703-061036_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b9ad9991-26a7-4000-9ff9-00baf052a846)
![Screenshot_20240703-061051_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e97d5799-62bd-4d7a-99c2-5c0e067a0485)
![Screenshot_20240703-061059_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8ac853de-f975-4745-a3f3-75f24b5521dc)
![Screenshot_20240703-061109_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/53559f39-a0a7-4537-a3c8-210a744484e2)
![Screenshot_20240703-061126_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/caeea8ff-cc9a-4b51-a228-8b99e2be60f0)
![Screenshot_20240703-061137_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6df0f801-8ec3-46f9-bc5c-2641f65d4549)
![Screenshot_20240703-061148_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f30cdbdd-dbc6-4715-8978-2a35accb4f2e)

## Tiny Bird + Snowflake
- Tiny Bird is a serverless ClickHouse https://www.youtube.com/watch?v=TcQolL2Xlic
	- Source connectors: kafka, snowflake,  etc.
	- Data pipelines separate stages

## Other databases
- TigerBeetle: World’s Fastest Financial Transactions Database https://www.youtube.com/watch?v=nTbQD30rk14
- QuestDB has been at the forefront of handling time series data with a focus on speed and efficiency https://www.youtube.com/watch?v=xneSPWsAuyI
