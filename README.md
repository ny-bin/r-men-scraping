# r-men-scraping

### Google Cloud Functions用のディレクトリ

1. 役割  
Google Cloud StrageにあるJson,XML,HTMLファイルを取得  
ファイル内を解析して、店舗データを取得し、DBに格納

2. 仕組み  
クローリング用のCloud FunctionsがページデータをStrageに格納  
→Strageに格納すると同時にCloud QueueにTaskをなげる  
→Taskを受け取ったQueueが、スクレイピング用のFunctionsにHTTPリクエストを送信  
→HTTPリクエストから解析するページデータをStrageから取得、DBに保存  


### デバッグ用メモ
ローカルでデバッグする際の手順  
・functions-frameworkを使用  
https://github.com/GoogleCloudPlatform/functions-framework-python

