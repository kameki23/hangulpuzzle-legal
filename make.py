"""한글 パズル 法務ページ生成: python3 make.py"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
APP = "한글 パズル"
UPDATED = "2026年10月27日"


def page(fname, title, desc, body, current):
    cur, hide = ' aria-current="page"', ' class="hide-sm"'
    nav = "".join(
        f'<a href="{h}"{cur if h == current else ""}{hide if h == "index.html" else ""}>{t}</a>'
        for h, t in [("index.html", "ホーム"), ("privacy.html", "プライバシー"), ("terms.html", "利用規約"), ("support.html", "サポート")])
    html = f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Zen+Old+Mincho:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<style>.app-icon{{width:96px;height:96px;border-radius:22px;display:block;margin-bottom:20px}}</style>
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true"></span>{APP}</a>
    <nav class="nav" aria-label="サイト内">{nav}</nav>
  </div>
</header>
{body}
<footer class="site-footer">
  <div class="wrap">
    <address>
      {APP} 運営：亀田直樹<br>
      お問い合わせ：<a href="mailto:work@turtlefit.jp">work@turtlefit.jp</a>
    </address>
    <nav aria-label="フッター">
      <a href="index.html">ホーム</a>
      <a href="privacy.html">プライバシーポリシー</a>
      <a href="terms.html">利用規約</a>
      <a href="support.html">サポート</a>
    </nav>
  </div>
  <div class="wrap" style="margin-top:20px">&copy; 2026 Naoki Kameda</div>
</footer>
</body>
</html>
"""
    open(os.path.join(HERE, fname), "w").write(html)


def doc(eyebrow, h1, inner):
    return f"""<main class="doc">
<div class="wrap">
  <div class="doc-head">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="updated">最終更新日：{UPDATED}</p>
  </div>
{inner}
</div>
</main>"""


page("index.html", f"{APP}｜パズルで続ける韓国語", "30日で韓国語の日常会話。タップで発音が聞ける、パズル式の韓国語学習アプリ。", """<main>
<section class="hero">
  <div class="wrap">
    <img class="app-icon" src="icon.png" alt="">
    <p class="eyebrow">HANGUL PUZZLE — 韓国語学習アプリ</p>
    <h1>30日で、<br><em>韓国語の日常会話。</em></h1>
    <p class="lead">한글 パズルは、ハングルの文字からあいさつ、カフェでの注文、買い物、道案内まで、1日1レッスンのパズル感覚で韓国語を身につける学習アプリです。</p>
    <span class="store" aria-label="App Storeで近日公開">App Store <small>近日公開</small></span>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2 class="section-title">主な機能</h2>
    <ul class="features">
      <li><span class="num">01</span><h3>1日1レッスン</h3><p>基礎編30日と応用編60日、全90日のカリキュラム。</p></li>
      <li><span class="num">02</span><h3>タップで発音</h3><p>単語・フレーズ・会話をタップすると韓国語の発音が流れます。ゆっくり再生も。</p></li>
      <li><span class="num">03</span><h3>3つのパズル</h3><p>ペアマッチ、聞き取り4択、文の並べ替えで覚えた表現を定着。</p></li>
      <li><span class="num">04</span><h3>会話練習</h3><p>場面ごとの会話を、相手のセリフを聞きながら学べます。</p></li>
      <li><span class="num">05</span><h3>復習と単語帳</h3><p>苦手な言葉やお気に入りから出題。覚えた言葉は単語帳に。</p></li>
      <li><span class="num">06</span><h3>登録不要</h3><p>アカウント登録なしですぐに始められます。学習記録は端末内に保存。プレミアムは広告なし。</p></li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2 class="section-title">ご案内</h2>
    <ul class="links">
      <li><a href="privacy.html">プライバシーポリシー <span>情報の取り扱い</span></a></li>
      <li><a href="terms.html">利用規約 <span>ご利用のルールとサブスクリプション</span></a></li>
      <li><a href="support.html">サポート・よくある質問 <span>お問い合わせ</span></a></li>
    </ul>
  </div>
</section>
</main>""", "index.html")

page("privacy.html", f"プライバシーポリシー｜{APP}", f"「{APP}」のプライバシーポリシー。", doc("PRIVACY POLICY", "プライバシーポリシー", f"""
  <p>亀田直樹（以下「運営者」）は、iOSアプリ「{APP}」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。</p>

  <h2>1. 運営者が取得する情報</h2>
  <p>運営者は、氏名・メールアドレス・電話番号・位置情報などの個人情報を取得しません。アカウント登録も不要です。ただし、無料でご利用の場合は、下記5のとおり広告配信事業者が端末の情報を取得します。</p>
  <p>学習の進み具合、連続学習日数、お気に入り、苦手な言葉、読み上げ速度、通知の設定は、利用者の端末内にのみ保存され、運営者のサーバーには送信されません。</p>

  <h2>2. 音声の読み上げ</h2>
  <p>韓国語の発音は、iOSに搭載された端末内の音声合成機能で再生します。本アプリはマイクを使用せず、録音も行いません。</p>

  <h2>3. 購入情報</h2>
  <p>プレミアム（自動更新サブスクリプション）の購入・決済はAppleのApp Storeを通じて行われ、運営者はクレジットカード情報などの決済情報を取得しません。購入状態の確認は、Appleが提供する仕組み（StoreKit）を通じて端末内で行います。</p>

  <h2>4. 通知</h2>
  <p>リマインダー通知は利用者が設定した場合のみ、端末内で予約されます。通知のために情報を外部へ送信することはありません。</p>

  <h2>5. 広告（Google AdMob）</h2>
  <p>本アプリは、無料でご利用の方に Google LLC が提供する広告配信サービス「Google AdMob」による広告を表示します。プレミアム会員には広告を表示しません。</p>
  <p>Google AdMob は、広告の配信・効果測定・不正防止のために、広告識別子（IDFA）、IPアドレス、端末やOSの種類、おおよその位置情報、広告の表示やタップの履歴などを取得することがあります。広告識別子はアプリ起動時の確認画面で「トラッキングを許可」した場合のみ使用され、許可しない場合はパーソナライズされていない広告が表示されます。設定はiPhoneの「設定」→「プライバシーとセキュリティ」→「トラッキング」からいつでも変更できます。</p>
  <p>Google による情報の取り扱いは、<a href="https://policies.google.com/technologies/partner-sites?hl=ja">Google のポリシー（パートナーのサイトやアプリを使用する際の Google によるデータ使用）</a>をご確認ください。本アプリは、このほかに外部の解析ツールを使用しません。</p>

  <h2>6. 第三者提供</h2>
  <p>運営者は、本アプリを通じて利用者の個人情報を取得しないため、第三者に提供することはありません（広告配信事業者による情報の取得は上記5のとおりです）。</p>

  <h2>7. データの削除</h2>
  <p>アプリの「設定」→「学習記録をリセット」で学習記録を削除できます。アプリを削除すると、端末内のすべてのデータが削除されます。</p>

  <h2>8. 改定</h2>
  <p>本ポリシーは必要に応じて改定することがあります。重要な変更がある場合は、本ページでお知らせします。</p>

  <h2>9. お問い合わせ</h2>
  <p>本ポリシーに関するお問い合わせは <a href="mailto:work@turtlefit.jp">work@turtlefit.jp</a> までご連絡ください。</p>
"""), "privacy.html")

page("terms.html", f"利用規約｜{APP}", f"「{APP}」の利用規約とサブスクリプションについて。", doc("TERMS OF USE", "利用規約", f"""
  <p>この利用規約（以下「本規約」）は、亀田直樹（以下「運営者」）が提供するiOSアプリ「{APP}」（以下「本アプリ」）の利用条件を定めるものです。本アプリを利用された時点で、本規約に同意したものとみなします。</p>

  <h2>第1条（サービス内容）</h2>
  <p>本アプリは、日本語話者向けの韓国語学習アプリです。Day 1〜7のレッスンは無料で、Day 8〜90のレッスンと関連機能はプレミアム（有料）でご利用いただけます。無料でご利用の場合は広告が表示され、プレミアムでは広告が表示されません。</p>

  <h2>第2条（プレミアム・自動更新サブスクリプション）</h2>
  <ul>
    <li>プラン名：{APP} プレミアム（月額）</li>
    <li>料金：月額480円（税込）。地域により価格が異なる場合があります。</li>
    <li>期間：1か月。期間終了時に自動的に更新されます。</li>
    <li>お支払いは購入確定時にApple IDのアカウントに請求されます。</li>
    <li>現在の期間が終了する24時間以上前に自動更新をオフにしない限り、期間終了前の24時間以内に次の期間分が請求されます。</li>
    <li>解約は、iPhoneの「設定」→「Apple ID」→「サブスクリプション」から行えます。解約後も期間の終了までプレミアムをご利用いただけます。</li>
    <li>購入後の返金は、Appleの定める手続きに従います。運営者は返金に関与できません。</li>
  </ul>
  <p>本アプリの利用には、Appleの標準使用許諾契約（<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">EULA</a>）も適用されます。</p>

  <h2>第3条（禁止事項）</h2>
  <ul>
    <li>本アプリの教材・画像・プログラムを無断で複製、転載、改変、配布する行為</li>
    <li>本アプリのリバースエンジニアリング、または不正な方法で有料機能を利用する行為</li>
    <li>法令または公序良俗に反する行為</li>
  </ul>

  <h2>第4条（知的財産権）</h2>
  <p>本アプリに含まれる教材、キャラクター、デザイン、プログラムの権利は運営者または正当な権利者に帰属します。</p>

  <h2>第5条（免責）</h2>
  <p>運営者は、教材の内容の正確性に努めますが、学習効果や特定の目的への適合性を保証するものではありません。発音は端末の音声合成機能によるもので、端末やiOSのバージョンにより聞こえ方が異なる場合があります。</p>
  <p>運営者は、本アプリの利用により生じた損害について、運営者の故意または重過失による場合を除き、責任を負いません。</p>

  <h2>第6条（サービスの変更・終了）</h2>
  <p>運営者は、事前の通知により本アプリの内容を変更し、または提供を終了することがあります。</p>

  <h2>第7条（規約の変更）</h2>
  <p>運営者は、必要に応じて本規約を変更できるものとします。変更後の規約は本ページに掲載した時点から効力を生じます。</p>

  <h2>第8条（準拠法・管轄）</h2>
  <p>本規約は日本法に準拠し、本アプリに関する紛争は広島地方裁判所を第一審の専属的合意管轄裁判所とします。</p>
"""), "terms.html")

page("support.html", f"サポート｜{APP}", f"「{APP}」のサポート・よくある質問。", doc("SUPPORT", "サポート・よくある質問", f"""
  <h2>お問い合わせ</h2>
  <p>本アプリに関するご質問・不具合のご報告・教材の誤りのご指摘は、以下のメールアドレスまでお送りください。</p>
  <a class="mail" href="mailto:work@turtlefit.jp?subject=%ED%95%9C%EA%B8%80%20%E3%83%91%E3%82%BA%E3%83%AB%20%E3%81%8A%E5%95%8F%E3%81%84%E5%90%88%E3%82%8F%E3%81%9B">work@turtlefit.jp</a>
  <p>お使いの端末とiOSのバージョン、該当するDAY、内容をできるだけ詳しくお書きください。</p>

  <h2>よくある質問</h2>
  <div class="faq">
    <details><summary>音声が鳴りません。</summary><div class="a">
      <p>iPhoneの音量と、本体横の消音スイッチ（サイレントモード）をご確認ください。改善しない場合は、「設定」アプリ→「アクセシビリティ」→「読み上げコンテンツ」→「声」→「韓国語」から音声をダウンロードすると、より自然な発音で再生されます。</p>
    </div></details>
    <details><summary>無料で使える範囲は？</summary><div class="a">
      <p>Day 1〜7（ハングルの文字・あいさつ・お礼とおわび）のレッスンと、その範囲の復習・単語帳は無料でご利用いただけます。</p>
    </div></details>
    <details><summary>プレミアムを解約するには？</summary><div class="a">
      <p>iPhoneの「設定」→「Apple ID（お客様の名前）」→「サブスクリプション」→「{APP}」から解約できます。現在の期間が終了する24時間以上前に解約しない限り自動で更新されます。解約後も期間の終了まではプレミアムをご利用いただけます。</p>
    </div></details>
    <details><summary>機種変更や再インストール後にプレミアムを復元するには？</summary><div class="a">
      <p>購入時と同じApple IDでサインインした状態でアプリを開き、「設定」またはプレミアムの画面にある「購入を復元」をタップしてください。</p>
    </div></details>
    <details><summary>学習記録は引き継げますか？</summary><div class="a">
      <p>学習記録は端末内に保存されるため、機種変更時は引き継がれません（iCloudバックアップから復元した場合は引き継がれることがあります）。プレミアムの購入状態は「購入を復元」で引き継げます。</p>
    </div></details>
  </div>

  <h2>関連ページ</h2>
  <ul>
    <li><a href="privacy.html">プライバシーポリシー</a></li>
    <li><a href="terms.html">利用規約</a></li>
  </ul>
"""), "support.html")
print("ok")
