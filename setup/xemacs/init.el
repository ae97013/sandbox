;;; .xemacs/init.el

(set-face-foreground 'default "black")
(set-face-background 'default "white")
(display-time)                          ; Display the time on modeline
(line-number-mode t)                    ; Display the line number on modeline
(column-number-mode t)                  ; Display the column number on modeline
(setq-default kill-whole-line t)        ; Ctrl-k kills whole line if at col 0
(setq-default fill-column 75)           ; Wrap at col 75
(setq-default tab-width 8)              ; Show tabs as 8 cols
(setq-default transient-mark-mode t)    ; Turn on transient mark mode
(setq inhibit-startup-message t)        ; No welcome message
(setq minibuffer-max-depth nil)
(setq font-lock-auto-fontify t)         ; Font lock mode
(setq require-final-newline t)          ; Always end a file with a newline

;;; uncomment this line to disable loading of "default.el" at startup
;; (setq inhibit-default-init t)

;;
;; Needed packages
;; 

; enable syntax highlighting
(require 'font-lock)

(require 'jka-compr)
(auto-compression-mode 1)

;; Handy little redo function.
(require 'redo)
(global-set-key [(control x)(control r)] 'redo)

(require 'info)
;; (require 'diction)
(require 'tex-site)
(unless (featurep 'xemacs)
  (require 'html-helper-mode))
(require 'psgml)
(require 'w3)

;; Load my lynx viewing mode
(unless (featurep 'xemacs)
  (require 'lynx)
  (require 'mutt))
(require 'htmlize)
;; (require 'dired-single)

;; load xcscope
(require 'xcscope)

;; load python
(require 'python-mode)

;; don't let `next-line' add new lines in buffer
(setq next-line-add-newlines nil)

;; enable wheelmouse support by default
(when window-system
  (mwheel-install))

(global-set-key [home] 'beginning-of-line)
(global-set-key [end] 'end-of-line)
(global-set-key [delete] 'delete-char)

; how to do correct BS / DEL handling???
(global-set-key [backspace] 'backward-delete-char)
(global-set-key [del]       'delete-char)

; print
;;'(ps-lpr-switches (quote (
(setq-default debug-on-error nil)
(setq-default debug-on-quit nil)
(setq-default ps-lpr-command "lp")
;;(setq-default lpr-switches '("-P" "-c" "-d" "i11ps_ux1"))
;;(setq-default ps-lpr-switches '("-c" "-d" "i11ps_ux1"))
(setq-default lpr-switches '("-P" "-c"))
(setq-default ps-lpr-switches '("-c"))
(setq-default ps-print-color-p nil)
(setq ps-postscript-code-directory "/usr/share/emacs/21.5/etc")

(autoload 'ps-print-buffer "ps-print" "Load ps-print" t)
(autoload 'ps-spool-buffer "ps-print" "Load ps-print" t)

;; function keys
;; 1 - help, 2 - save, 3 - load, 4 - goto, 5 - zoom, 6 - next,
;; 7 - split, 8 - exit!, 9 - make, 10 - other, 11 - hilit, 12 - undo.
;; emacs: must use command name to allow interactive input

(global-set-key [f1] 'info)
(global-set-key [f2] 'save-buffer)
(global-set-key [f3] 'find-file)
(global-set-key [f4] 'goto-line)
(global-set-key [f5] 'delete-other-windows)
(global-set-key [f6] 'other-window)
(global-set-key [f7] 'previous-error)
(global-set-key [f8] 'next-error)
(global-set-key [f9] 'compile)
(global-set-key [f10] 'kill-buffer)
;;(global-set-key [f11] 'hilit-rehighlight-buffer)
(global-set-key [(f11)] (lambda () (interactive) (manual-entry (current-word))))
(global-set-key [f12] 'undo)

(global-set-key [(control f3)]  'cscope-set-initial-directory)
(global-set-key [(control f4)]  'cscope-unset-initial-directory)
(global-set-key [(control f5)]  'cscope-find-this-symbol)
(global-set-key [(control f6)]  'cscope-find-global-definition)
(global-set-key [(control f7)]  'cscope-find-global-definition-no-prompting)
(global-set-key [(control f8)]  'cscope-pop-mark)
(global-set-key [(control f9)]  'cscope-next-symbol)
(global-set-key [(control f10)] 'cscope-next-file)
(global-set-key [(control f11)] 'cscope-prev-symbol)
(global-set-key [(control f12)] 'cscope-prev-file)
(global-set-key [(meta f9)]  'cscope-display-buffer)
(global-set-key [(meta f10)] 'cscope-display-buffer-toggle)

;; C
(add-hook 'c-mode-common-hook 'my-c-mode-common-hook)
(defun my-c-mode-common-hook ()
  (define-key c-mode-map "\C-m" 'newline-and-indent)
  (c-set-style "K&R")
  (setq tab-width 8)
  (setq indent-tabs-mode t)
  (setq c-basic-offset 8)
  (set-fill-column 80))

(defun linux-c-mode ()
  "C mode with adjusted defaults for use with the Linux kernel."
  (interactive)
  (c-mode)
  (c-set-style "K&R")
  (setq tab-width 8)
  (setq indent-tabs-mode t)
  (setq c-basic-offset 8))

;; C++
(add-hook 'c++-mode-common-hook 'my-c++-mode-common-hook)
(defun my-c++-mode-common-hook ()
  (define-key c-mode-map "\C-m" 'newline-and-indent)
  (c-set-style "K&R")
  (setq c-basic-offset 8)
  (set-fill-column 80))

;; XML
(add-hook 'xml-mode-hook 'my-xml-mode-hook)
(defun my-xml-mode-hook ()
  (setq sgml-indent-data t))

;; Java
(add-hook 'java-mode-hook 'my-java-mode-hook)
(defun my-java-mode-hook ()
  (make-local-variable 'write-contents-hooks)
  (add-hook 'write-contents-hooks 'text-mode-untabify))

;; Perl
;; Use cperl-mode instead of the default perl-mode
(add-to-list 'auto-mode-alist '("\\.\\([pP][Llm]\\|al\\)\\'" . cperl-mode))
(add-to-list 'interpreter-mode-alist '("perl" . cperl-mode))
(add-to-list 'interpreter-mode-alist '("perl5" . cperl-mode))
(add-to-list 'interpreter-mode-alist '("miniperl" . cperl-mode))

(add-hook 'cperl-mode-hook 'my-cperl-mode-hook)
(defun my-cperl-mode-hook ()
  (cperl-set-style "PerlStyle")
  (imenu-add-to-menubar "Functions")
  (define-key cperl-mode-map [return] 'newline-and-indent)
  (define-key cperl-mode-map [f6] 'perl-run))

;; Python
(add-to-list 'auto-mode-alist '("\\.py\\'" . python-mode))
(add-to-list 'interpreter-mode-alist '("python" . python-mode))

(add-hook 'python-mode-hook 'my-python-mode-hook)
(defun my-python-mode-hook ()
  (local-set-key '[f4] 'pdb)
  (setq tab-width 4)
  (setq python-indent 4)
  (setq python-continuation-offset 4)
  (setq py-smart-indentation nil))
