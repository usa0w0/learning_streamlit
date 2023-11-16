# learning_streamlit
Python用webアプリライブラリのStreamlitについての勉強と久しぶりにgit運用の練習

## 目的
- Streamlitの使い方を学ぶ
- GithubおよびGitの使い方を復習する
  - cloneではなく、既存のディレクトリからリモート連携を行う
- 作業録を作る

## 作業ディレクトリとリモートリポジトリの準備
- 作業ディレクトリの作成
  ```ターミナル
  mkdir ディレクトリ名
  ```

- 作成したディレクトリをVScodeで開く（現在のディレクトリを開く）
  ```ターミナル
  code .
  ```
  ※ `code`コマンドが使用できない場合 → VScodeのコマンドパレットから、`シェルコマンド:PATH内に’code’コマンドをインストールします`で起動コマンドをインストール

- 適当なファイルを作成（実行確認）
  ```app.py
  print('Hi friends!')
  ```
  ※ 一応のメモとして仮想環境の作成 by Anaconda
  ```ターミナル
  conda create -n 仮想環境名
  conda activate 仮想環境名
  ```

- Githubにリポジトリ作成：ブラウザ等でぽちぽちしてください

- リポジトリ連携
  - ローカルリポジトリの作成（作業ディレクトリをGit管理化）
    ```ターミナル
    git init
    ```

  - リモートリポジトリ設定（SSH）
    ```ターミナル
    git remote add origin git@github.com:ユーザー名/リポジトリ名.git
    ```
  
  - 既存ファイルの追加
    ```ターミナル
    git add ファイル名
    git commit -m コミットメッセージ
    git push -u origin main
    ```
    ※ リモートへのpushは、`git push origin main`でも可。`push`時に`-u`オプションをつけておくと、上流ブランチの設定もできるため、後々楽。

    上流ブランチの設定
    ```ターミナル
    git branch -u origin/ブランチ名
    ```

