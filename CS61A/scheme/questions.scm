(define (caar x) (car (car x)))

(define (cadr x) (car (cdr x)))

(define (cdar x) (cdr (car x)))

(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement
(define (zip pairs)
  (define (caarer s)
    (if (null? s) () (cons (caar s) (caarer (cdr s))))
  )
  (define (cdarer s)
    (if (null? s) () (cons (car (cdar s)) (cdarer (cdr s))))
  )
  (cons (caarer pairs) (list (cdarer pairs)))
  )

; ; Problem 15
; ; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (helper counter z)
           (cond
             ((null? z)
              ())
             (else (cons (list counter (car z)) (helper (+ counter 1) (cdr z))))))
         (helper 0 s)
         )

; END PROBLEM 15
; ; Problem 16
; ; Merge two lists LIST1 and LIST2 according to COMP and return
; ; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond ((null? list1) list2)
  ((null? list2) list1)
  ((comp (car list1) (car list2)) (cons (car list1) (merge comp (cdr list1) list2)) )
    (else (cons (car list2) (merge comp list1 (cdr list2)))))
    )

; END PROBLEM 16
(merge < '(1 5 7 9) '(4 8 10))

; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))

; expect (10 9 8 7 5 4 3 1)
; ; Problem 17
(define (nondecreaselist s)
  ; BEGIN PROBLEM 17
  (define (increasing s) (cond ((null? (cdr s)) (cons (car s) nil))
    ((> (car s) (cadr s)) (cons (car s) nil)) (else (cons (car s) (increasing (cdr s))))))

  (define (decreasing s) (cond ((null? (cdr s)) ())
    ((> (car s) (cadr s))  s) (else (decreasing (cdr s)))))
  ; use cdr of decreasing

  (cond ((null? s) ()) ((null? (decreasing s)) (cons s nil)) ((null? (cdr (decreasing s))) (cons s nil))
  (else (cons (increasing s) (nondecreaselist (cdr (decreasing s))) ))))


; END PROBLEM 17
; ; Problem EC
; ; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))

(define define? (check-special 'define))

(define quoted? (check-special 'quote))

(define let? (check-special 'let))

; ; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond
    ((atom? expr)
     ; BEGIN PROBLEM EC
     expr
     ; END PROBLEM EC
    )
    ((quoted? expr)
     ; BEGIN PROBLEM EC
     expr
     ; END PROBLEM EC
    )
    ((or (lambda? expr) (define? expr))
     (let ((form (car expr))
           (params (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM EC
       (cons form (cons params  (map let-to-lambda body) ))
       ; END PROBLEM EC
     ))
    ((let? expr)
     (let ((values (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM EC
       (cons (cons 'lambda (cons (car (zip values))  (map let-to-lambda body))) (map let-to-lambda (cadr (zip values))))
       ; END PROBLEM EC
     ))
    (else
     ; BEGIN PROBLEM EC
     (map let-to-lambda expr)
     ; END PROBLEM EC
    )))
