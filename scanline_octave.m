function img = scanline(buf, lista_poligono, intensidade):
    img = buf;

    y_minimo = min(lista_poligono)(2);
    y_maximo = max(lista_poligono)(2);

    for y = y_minimo:y_maximo

        i = [];

        ponto_inicial_x = lista_poligono(1,1);
        ponto_inicial_y = lista_poligono(1,2);

        for p = 2:rows(poligono)
            ponto_final_x = lista_poligono[p][1];
            ponto_final_y = lista_poligono[p][2];

            x_intersecao = round(intersecao(y, [ponto_inicial_x ponto_inicial_y; ponto_final_x ponto_final_y]));

            if x_intersecao >= 0
                i = [i x_intersecao]
            endif

            ponto_inicial_x = ponto_final_x;
            ponto_inicial_y = ponto_final_y;

        endfor

        ponto_final_x = lista_poligono(1, 1);
        ponto_final_y = lista_poligono(1, 2);

        x_intersecao = round(intersecao(y, [ponto_inicial_x ponto_inicial_y; ponto_final_x ponto_final_y]));

        if x_intersecao >= 0
            i = [i x_intersecao]
        endif

        for ponto_intersecao = 1:2:length(i)
            for pixel = i(ponto_intersecao):i(ponto_intersecao+1)
                img = setpixel(img, pixel, y, intensidade);
            endfor
        endfor
    endfor
endfunction