set nocompatible              " be iMproved, required 
filetype off                  " required 

" set the runtime path to include Vundle and initialize 
set rtp+=~/.vim/bundle/vundle/
call vundle#rc() 
" alternatively, pass a path where Vundle should install plugins 
"call vundle#begin('~/some/path/here') 
" let Vundle manage Vundle, required 
Plugin 'gmarik/Vundle.vim' 


" Status bar
Plugin 'vim-airline/vim-airline'
Plugin 'tpope/vim-fugitive'

" highlight the matched tag 
Plugin 'gregsexton/MatchTag' 

"map <Leader>m <Plug>(easymotion-prefix) 
" <Leader>mw: select a beginning of word to jump 
" <Leader>mW: select a beginning of WORD to jump 
" <Leader>mf: select a right char to jump 
" <Leader>mF: select a left char to jump 
" <Leader>mj: select a line downward to jump 
" <Leader>mk: select a line forward to jump 
" and so on 
" <Leader>mn: select a latest / or ? to jump 
" <Leader>mN: select a latest / or ? to jump 
" <Leader>ms: select a right and left char to jump 
Plugin 'easymotion/vim-easymotion' 

" :TagbarToggle 
" <Leader>l 
" p : preview 
" s : trigger sort 

Plugin 'majutsushi/tagbar' 

" syntax 
Plugin 'othree/html5.vim' 
Plugin 'syntax/css.vim' 
Plugin 'elzr/vim-json' 
Plugin 'scrooloose/syntastic'

filetype plugin indent on    " required 

" To ignore plugin indent changes, instead use: 
"filetype plugin on 
"
" Brief help 
" :PluginList          - list configured plugins 
" :PluginInstall(!)    - install (update) plugins 
" :PluginSearch(!) foo - search (or refresh cache first) for foo 
" :PluginClean(!)      - confirm (or auto-approve) removal of unused plugins 
" 

" see :h vundle for more details or wiki for FAQ 

" Put your non-Plugin stuff after this line 

" Set tab

Plugin 'mattn/emmet-vim'
Plugin 'pangloss/vim-javascript'
Plugin 'mxw/vim-jsx'

set expandtab 
set tabstop=4 
set shiftwidth=4
set number

let g:jsx_ext_required = 0 

highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%81v.\+/
set mouse=n

let g:syntastic_javascript_checkers = ['eslint']
let g:syntastic_always_populate_loc_list = 1

let g:javascript_plugin_jsdoc = 1
let g:javascript_plugin_flow = 1

let g:javascript_conceal_arrow_function = "⇒"

Plugin 'nathanaelkane/vim-indent-guides'

let g:indent_guides_auto_colors = 0
hi IndentGuidesOdd  ctermbg=DarkGray
hi IndentGuidesEven ctermbg=Black

let g:indent_guides_start_level = 1
let g:indent_guides_guide_size = 1

