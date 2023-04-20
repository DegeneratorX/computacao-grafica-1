function m = setpixel(img, x, y, intensidade)
  m = img;
  x = x + 1;
  y = y + 1;
  if x < 1
    x = 1;
  endif
  if y < 1
    y = 1;
  endif
  if x > columns(m)
    x = columns(m);
  endif
  if y > rows(m)
    y = rows(m);
  endif
  m(y,x) = intensidade;
endfunction