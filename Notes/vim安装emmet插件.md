# vim 安装emmet插件



## 1. vim基本配置
vim的基本配置可以使用 [spf13-vim](https://github.com/spf13/spf13-vim)的配置。

建议在普通用户下进行安装，执行以下命令，慢慢等待安装完成。

```
$ curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh
```

## 2. 安装emmet插件

vim下可以用的emmet插件在github的地址[mattn/emmet-vim](https://github.com/mattn/emmet-vim)

先从github上面clone emmet的代码。

```
$ cd ~/.vim/bundle
$ git clone https://github.com/mattn/emmet-vim.git
```

修改spf13-vim的配置，spf13-vim中bundles的配置都在`.vimrc.bundles`中。

```
$ vim .vimrc.bundles
```

大约在250行的位置，增加一行`Bundle 'mattn/emmet-vim'`，保存退出。

```
" HTML {    
if count(g:spf13_bundle_groups, 'html')
    Bundle 'amirh/HTML-AutoCloseTag'
    Bundle 'hail2u/vim-css3-syntax'
    Bundle 'gorodinskiy/vim-coloresque'
    Bundle 'tpope/vim-haml'
    Bundle 'mattn/emmet-vim'
endif
" }
```

然后重新打开vim编辑器，运行`:BundleInstall`，进行插件安装。

## 3. emmet插件的使用

输入emmet语法后，先按 `<ctrl+y>` 再按 `,`

## 参考

[spf13/spf13-vim](https://github.com/spf13/spf13-vim)
[Vim学习再开（2）——Emmet for Vim](http://nerd-is.in/2013-12/learn-vim-again-2-emmet-for-vim/)