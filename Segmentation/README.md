# 五官分割文档示例

该项目为五官分割文档示例，该示例**无法在线调试**，如需调试可下载到本地后替换 [AK](https://usercenter.console.aliyun.com/#/manage/ak) 以及参数后进行调试。

## 运行条件

- 下载并解压需要语言的代码;

- 在阿里云帐户中获取您的 [凭证](https://usercenter.console.aliyun.com/#/manage/ak)并通过它替换下载后代码中的 ACCESS_KEY_ID 以及 ACCESS_KEY_SECRET;

- 执行对应语言的构建及运行语句

## 执行步骤
下载的代码包，在根据自己需要更改代码中的参数和 AK 以后，可以在**解压代码所在目录下**按如下的步骤执行

- Java
*JDK 版本要求 1.8*
```sh
mvn clean package
java -jar target/sample-1.0.0-jar-with-dependencies.jar
```

- TypeScript
*Node 版本要求 10.x 及以上*
```sh
npm install --registry=https://registry.npm.taobao.org && tsc && node ./dist/client.js
```

- Go
*Golang 版本要求 1.13 及以上*
```sh
GOPROXY=https://goproxy.cn,direct go run ./main
```

- PHP
*PHP 版本要求 7.2 及以上*
```sh
composer install && php src/Sample.php
```

- Python
*Python 版本要求 Python3*
```sh
python3 setup.py install && python ./alibabacloud_sample/sample.py
```

- C#
*.NETCORE 版本要求 2.1及以上*
```sh
cd ./core && dotnet run
```

## 使用的 API

-  ParseFace 五官分割文档示例，可以参考：[文档](https://next.api.aliyun.com/document/imageseg/2019-12-30/ParseFace)



## 返回示例

*实际输出结构可能稍有不同，属于正常返回；下列输出值仅作为参考，以实际调用为准*


- JSON 格式 
```js
{
	"RequestId": "D6C24839-91A7-41DA-B31F-98F08EF80CC0",
	"Data": {
		"OriginImageURL": "https://vigen-invi.oss-cn-shanghai.aliyuncs.com/temp/faceparsing/example.jpg",
		"Elements": [{
				"Name": "skin",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751202611000042_EBPBLN.png"
			},
			{
				"Name": "l_brow",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751204181000049_fTTYNi.png"
			},
			{
				"Name": "r_brow",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751205391000051_ydEwL5.png"
			},
			{
				"Name": "l_eye",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751206401000054_m6dPH2.png"
			},
			{
				"Name": "r_eye",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751207281000055_nH722a.png"
			},
			{
				"Name": "l_ear",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751202771000044_xzaQjz.png"
			},
			{
				"Name": "r_ear",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751203891000047_e9cPUx.png"
			},
			{
				"Name": "nose",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751204921000050_1mGUOK.png"
			},
			{
				"Name": "u_lip",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751202751000043_tIPX7W.png"
			},
			{
				"Name": "l_lip",
				"ImageURL": "oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751203701000046_K8aiYg.png"
			}
		]

	}
}
```
- XML 格式 
```xml
<RequestId>D6C24839-91A7-41DA-B31F-98F08EF80CC0</RequestId>
<Data>
    <OriginImageURL>https://vigen-invi.oss-cn-shanghai.aliyuncs.com/temp/faceparsing/example.jpg</OriginImageURL>
    <Elements>
        <Name>skin</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751202611000042_EBPBLN.png</ImageURL>
    </Elements>
    <Elements>
        <Name>l_brow</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751204181000049_fTTYNi.png</ImageURL>
    </Elements>
    <Elements>
        <Name>r_brow</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751205391000051_ydEwL5.png</ImageURL>
    </Elements>
    <Elements>
        <Name>l_eye</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751206401000054_m6dPH2.png</ImageURL>
    </Elements>
    <Elements>
        <Name>r_eye</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi_builder_015814751207281000055_nH722a.png</ImageURL>
    </Elements>
    <Elements>
        <Name>l_ear</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751202771000044_xzaQjz.png</ImageURL>
    </Elements>
    <Elements>
        <Name>r_ear</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751203891000047_e9cPUx.png</ImageURL>
    </Elements>
    <Elements>
        <Name>nose</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751204921000050_1mGUOK.png</ImageURL>
    </Elements>
    <Elements>
        <Name>u_lip</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751202751000043_tIPX7W.png</ImageURL>
    </Elements>
    <Elements>
        <Name>l_lip</Name>
        <ImageURL>oss://viapi-cn-shanghai-dha-segmenter/upload/fivesensesegmenter-2020-02-11-19-58-42-cd987d5f8-jxqn4/2020-2-12/invi__015814751203701000046_K8aiYg.png</ImageURL>
    </Elements>
</Data>
```


