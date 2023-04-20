function img = retaDDAAA(buf, xi, yi, xf, yf, intensidade)
  
  img = buf;
  
  dx = xf-xi;
  dy = yf-yi;
  
  passos = abs(dx);
  if abs(dy) > abs(dx)
    passos = abs(dy);
  endif
  
  if passos == 0
    img = setpixel(img, xi, yi, intensidade);
    return;
  endif
  
  passox = dx/passos;
  passoy = dy/passos;
  
  for i = 0:passos
    x = xi + i*passox;
    y = yi + i*passoy;
    
    if abs(round(passox)) == 1
       yd = y - floor(y);
    
       img = setpixel(img, round(x), floor(y),   round((1-yd)*intensidade));
       img = setpixel(img, round(x), floor(y+1), round(yd*intensidade));
    else
       xd = x - floor(x);
    
       img = setpixel(img, floor(x), round(y),   round((1-xd)*intensidade));
       img = setpixel(img, floor(x+1), round(y), round(xd*intensidade));
        
    endif
  endfor
  
endfunction