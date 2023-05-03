# code_portfolio_data_scientist
code_portfolio_data_scientist


learn from https://github.com/alshedivat/al-folio


将 rbenv init 添加到您的 shell 配置文件（例如 ~/.bashrc 或 ~/.zshrc）：” 我不确定我的版本是。~/.bashrc 或 ~/.zshrc 这个版本在哪里，如何查询？

要确定您正在使用的 shell，可以打开一个终端窗口并运行以下命令：

bash
Copy code
echo $SHELL
这将输出您正在使用的 shell，例如 /bin/bash 或 /bin/zsh。


根据输出的结果，您可以选择相应的配置文件。如果输出是 /bin/bash，则配置文件通常是 ~/.bashrc 或 ~/.bash_profile。如果输出是 /bin/zsh，则配置文件是 ~/.zshrc。

kang@Love-Grace al-folio$ echo $SHELL
/bin/bash

我们是：
ls ~/.bashrc
/Users/kang/.bashrc
这是我们的配置文件。
subl ~./.bashrc：
[ -f "/Users/kang/.ghcup/env" ] && source "/Users/kang/.ghcup/env" # ghcup-env
export PATH="/opt/homebrew/bin:$PATH"

if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi

----

接下来，运行以下命令以启动本地Jekyll服务器：
bundle exec jekyll serve --lsi

  Populating LSI... 
Rebuilding index... 
                    
                    done in 39.665 seconds.
 Auto-regeneration: enabled for '/Users/kang/1.live_wit_GPT4/code_portfolio_data_scientist/al-folio'
    Server address: http://127.0.0.1:4000/al-folio/
  Server running... press ctrl-c to stop.

 du -sh al-folio/
153M	al-folio/


---
尽管 PythonAnywhere 主要针对 Python 项目，但您仍然可以在其中部署 Jekyll（Ruby）项目。为了实现这一点，您需要利用 PythonAnywhere 的 Bash 控制台功能。

请按照以下步骤在 PythonAnywhere 上部署 Jekyll 项目：

登录到您的 PythonAnywhere 账户。
转到 "Web" 选项卡并创建一个新的 Web 应用程序。选择 "Manual Configuration"，然后选择 "Python" 作为运行时（尽管我们实际上将运行 Jekyll，而不是 Python 代码）。
转到 "Consoles" 选项卡，然后打开一个新的 Bash 控制台。
在 Bash 控制台中，运行以下命令来安装 Jekyll 和 Bundler：gem install jekyll bundler
使用 git clone 命令克隆您的 Jekyll 项目到 PythonAnywhere。
进入项目目录，运行 bundle install 安装依赖项。
在项目目录中，运行 jekyll build 以生成站点。
转到 "Web" 选项卡，然后在 "Code" 部分将 "Source code" 和 "Working directory" 设置为您的 Jekyll 项目目录。
在 "Static files" 部分，将 URL 设置为 /，将 "Directory" 设置为您的 Jekyll 项目中 _site 目录的路径。
单击 "Reload" 按钮以重新加载 Web 应用程序。
现在，您的 Jekyll 站点应该在您指定的 PythonAnywhere 域名上运行。请注意，每当您更新项目内容时，您需要在 Bash 控制台中运行 jekyll build 命令以重新生成站点。您还需要确保安装了所有必要的依赖项。
----
al-folio$ find . -name "prof_pic-1400.webp"
./_site/assets/img/prof_pic-1400.webp

grep -r "prof_pic-1400.webp" .

--
    <source class="responsive-img-srcset" media="(max-width: 480px)" srcset="/al-folio/assets/img/prof_pic-480.webp"></source>
    <source class="responsive-img-srcset" media="(max-width: 800px)" srcset="/al-folio/assets/img/prof_pic-800.webp"></source>
    <source class="responsive-img-srcset" media="(max-width: 1400px)" srcset="/al-folio/assets/img/prof_pic-1400.webp"></source>
    
    -----


kang@Love-Grace al-folio$ grep -r "responsive-img-srcset" ./_includes
./_includes/figure.html:        class="responsive-img-srcset"
./_includes/figure.html:      onerror="this.onerror=null; $('.responsive-img-srcset').remove();"


---

实际上，人家已经写得非常清楚了：

XIAOWEN KANG

Affiliations. Address. Contacts. Moto. Etc.
prof_pic.jpg

555 your office number

123 your address street

Your City, State 12345

Write your biography here. Tell the world about yourself. Link to your favorite subreddit. You can put a picture in, too. The code is already in, just name your picture prof_pic.jpg and put it in the img/ folder.

Put your address / P.O. box / other info right below your picture. You can also disable any of these elements by editing profile property of the YAML header of your _pages/about.md. Edit _bibliography/papers.bib and Jekyll will render your publications page automatically.

Link to your social media connections, too. This theme is set up to use Font Awesome icons and Academicons, like the ones below. Add your Facebook, Twitter, LinkedIn, Google Scholar, or just disable all of them.

-----

--很好。我们做项目好了。这些东西，其实并不太重要。仅仅是勇于自己的分析和展示。 
我需要加油了。 





