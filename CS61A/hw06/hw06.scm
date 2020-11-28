(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr(cdr s)))
)


(define (sign num)
  (cond
  ((> num 0) 1)
  ((= num 0) 0)
  (else -1))
)


(define (square x) (* x x))

(define (pow x y)
  (cond
  ((= x 1) 1)
  ((= y 1) x)
  ((= (remainder y 2) 1) (* x (square (pow x (quotient (- y 1) 2)))))
  ((= (remainder y 2) 0) (square (pow x (quotient y 2)))))
)
