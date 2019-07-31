def runMatrixCh(Matrix,N,M):
  c = N//2
  newMatrix = []
  n = 0
  m = 0
  C = 1
  if c < 1 :
    for i in range(M):
      if i == 0:
        for j in range(N):
          if j == 0:
            newMatrix.append(Matrix[i+1*N])
          else:
            newMatrix.append(Matrix[j - 1])
      elif 0 < i + 1 < N:
        for j in range(N):
          if 0 < i + 1 < N and j == 0:
            newMatrix.append(Matrix[N * (i+1)])
          elif 0 < i + 1 < N and j+1 < N:
            newMatrix.append(Matrix[N+j])
          elif 0 < i + 1 < N and j+1 == N:
            newMatrix.append(Matrix[N*i-1])
      elif i + 1 == N:
        for j in range(N):
          if i+1 == N and j == 0:
            newMatrix.append(Matrix[N * (j + 2) + 1])
          elif i+1 == N and j+1 < N:
            newMatrix.append(Matrix[(j + 1) * N + N - 1])
          elif i+1 == N and j+1 == N:
            newMatrix.append(Matrix[N*i-1])
  else:
    for i in range(M):
      if i == 0: # 1 ряд матрицы
        for j in range(N):
          if j == 0:
            newMatrix.append(Matrix[i+N])
            n += 1
          else:
            newMatrix.append(Matrix[j - 1])
      elif i > 0 and i+1 < N: # со второго до пред последнего ряда
        if C > 0 and n < c and m < c :
          n += 1
          m += 1
          for j in range(N):
            if j < n:
              newMatrix.append(Matrix[N * (i + 1) + j])
            elif j >= n and j < N - m:
              newMatrix.append(Matrix[N*i+j-1])
            else:
              newMatrix.append(Matrix[N*(i-1)+j])
        else:
          if m >= c:
            n -= 1
            m -= 1
            for j in range(N):
              if j < n:
                newMatrix.append(Matrix[N * (i + 1) + j])
              elif j >= n and j < N - m:
                newMatrix.append(Matrix[N*i+j+1])
              else:
                newMatrix.append(Matrix[N*(i-1)+j])
          else:
            n-= 1
            m += 1
            for j in range(N):
              if j < n:
                newMatrix.append(Matrix[N * (i + 1) + j])
              elif j >= n and j < N - m:
                newMatrix.append(Matrix[N*i+j+1])
              else:
                newMatrix.append(Matrix[N*(i-1)+j])
            c -= 1
      elif i + 1 == N: # последний ряд матрицы
        for j in range(N):
          if j+1 < N:
            newMatrix.append(Matrix[N * i + 1 + j])
          elif j+1 == N:
            newMatrix.append(Matrix[N * i - 1])
            n += 1
  return newMatrix

def runMatrixChN(Matrix,M,N):
  c = M//2
  newMatrix = []
  n = 0
  m = 0
  C = 1
  if c < 1 :
    for i in range(M):
      if i == 0:
        for j in range(N):
          if j == 0:
            newMatrix.append(Matrix[i+1*N])
          else:
            newMatrix.append(Matrix[j - 1])
      elif 0 < i + 1 < N:
        for j in range(N):
          if 0 < i + 1 < N and j == 0:
            newMatrix.append(Matrix[N * (i+1)])
          elif 0 < i + 1 < N and j+1 < N:
            newMatrix.append(Matrix[N+j])
          elif 0 < i + 1 < N and j+1 == N:
            newMatrix.append(Matrix[N*i-1])
      elif i + 1 == N:
        for j in range(N):
          if i+1 == N and j == 0:
            newMatrix.append(Matrix[N * (j + 2) + 1])
          elif i+1 == N and j+1 < N:
            newMatrix.append(Matrix[(j + 1) * N + N - 1])
          elif i+1 == N and j+1 == N:
            newMatrix.append(Matrix[N*i-1])
  else:
    for i in range(M):
      if i == 0: # 1 ряд матрицы
        for j in range(N):
          if j == 0:
            newMatrix.append(Matrix[i+N])
            n += 1
          else:
            newMatrix.append(Matrix[j - 1])
      elif i > 0 and i+1 < M: # со второго до пред последнего ряда
        if C > 0 and n < c and m < c :
          n += 1
          m += 1
          for j in range(N):
            if j < n:
              newMatrix.append(Matrix[N * (i + 1) + j])
            elif j >= n and j < N - m:
              newMatrix.append(Matrix[N*i+j-1])
            else:
              newMatrix.append(Matrix[N*(i-1)+j])
        else:
          if m >= c:
            for j in range(N):
              if j < n:
                newMatrix.append(Matrix[N * (i + 1) + j])
              elif j >= n and j < N - m:
                newMatrix.append(Matrix[N*i+j+1])
              else:
                newMatrix.append(Matrix[N*(i-1)+j])
            n -= 1
            m -= 1
          else:
            n -= 1
            m += 1
            for j in range(N):
              if j < n:
                newMatrix.append(Matrix[N * (i + 1) + j])
              elif j >= n and j < N - m:
                newMatrix.append(Matrix[N*(i+1)+j])
              else:
                newMatrix.append(Matrix[N*(i-1)+j])
            c -= 1
      elif i + 1 == M: # последний ряд матрицы
        for j in range(N):
          if j+1 < N:
            newMatrix.append(Matrix[N * i + 1 + j])
          elif j+1 == N:
            newMatrix.append(Matrix[N * i - 1])
            n += 1
  return newMatrix

def runMatrixChNM(Matrix,M,N):
  c = M//2
  newMatrix = []
  n = 0
  m = 0
  C = 1
  if c < 1 :
    for i in range(M):
      if i == 0:
        for j in range(N):
          if j == 0:
            newMatrix.append(Matrix[i+1*N])
          else:
            newMatrix.append(Matrix[j - 1])
      elif 0 < i + 1 < N:
        for j in range(N):
          if 0 < i + 1 < N and j == 0:
            newMatrix.append(Matrix[N * (i+1)])
          elif 0 < i + 1 < N and j+1 < N:
            newMatrix.append(Matrix[N+j])
          elif 0 < i + 1 < N and j+1 == N:
            newMatrix.append(Matrix[N*i-1])
      elif i + 1 == N:
        for j in range(N):
          if i+1 == N and j == 0:
            newMatrix.append(Matrix[N * (j + 2) + 1])
          elif i+1 == N and j+1 < N:
            newMatrix.append(Matrix[(j + 1) * N + N - 1])
          elif i+1 == N and j+1 == N:
            newMatrix.append(Matrix[N*i-1])
  else:
    for i in range(M):
      if i == 0: # 1 ряд матрицы
        for j in range(N):
          if j == 0:
            newMatrix.append(Matrix[i+N])
            n += 1
          else:
            newMatrix.append(Matrix[j - 1])
      elif i > 0 and i+1 < M: # со второго до пред последнего ряда
        if C > 0 and n < c and m < c :
          n += 1
          m += 1
          for j in range(N):
            if j < n:
              newMatrix.append(Matrix[N * (i + 1) + j])
            elif j >= n and j < N - m:
              newMatrix.append(Matrix[N*i+j-1])
            else:
              newMatrix.append(Matrix[N*(i-1)+j])
        else:
          if m >= c:
            for j in range(N):
              if j < n:
                newMatrix.append(Matrix[N * (i + 1) + j])
              elif j >= n and j < N - m:
                newMatrix.append(Matrix[N*i+j+1])
              else:
                newMatrix.append(Matrix[N*(i-1)+j])
            n -= 1
            m -= 1
          else:
            n -= 1
            m += 1
            for j in range(N):
              if j < n:
                newMatrix.append(Matrix[N * (i + 1) + j])
              elif j >= n and j < N - m:
                newMatrix.append(Matrix[N*i+1+j])
              else:
                newMatrix.append(Matrix[N*(i-1)+j])
            c -= 1
      elif i + 1 == M: # последний ряд матрицы
        for j in range(N):
          if j+1 < N:
            newMatrix.append(Matrix[N * i + 1 + j])
          elif j+1 == N:
            newMatrix.append(Matrix[N * i - 1])
            n += 1
  return newMatrix

def MatrixTurn(Matrix, M, N, T):
  n = 0
  j = 0
  result =[]
  res = []
  sb = []
  matt = []
  for i in range(len(Matrix)):
    for j in range(len(Matrix[i])):
      matt.append(Matrix[i][j])
  if M == N:
    for i in range(T):
      res = runMatrixCh(matt,M,N)

  elif M < N and M%2 == 0:
    if M*N != len(matt):
      return 'Неверно введены данные!'
    else:
      for i in range(T):
        res = runMatrixChNM(matt,M,N)
  elif N < M and N%2 == 0:
    if M*N != len(matt):
      return 'Неверно введены данные!'
    else:
      for i in range(T):
        res = runMatrixChN(matt,M,N)
  else:
    return 'Неверные данные!'
  Matrix.clear()
  for i in range(len(res)):
    if i%N == 0 and i != 0:
      Matrix.append(''.join(sb))
      sb.clear()
    sb.append(res[i])
    if i == len(res) - 1:
      Matrix.append(''.join(sb))
      sb.clear()