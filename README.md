#grid
US LOCATION Grid

    LAT                   LONG
    64.9552001953125      -66.08159637451172
    64.0                  -66.0
    17.996400833129883    -123.99700164794922
    18.0                  -124.0

Output

    Count : 266,800

    [
        (64.0, -66.0), (63.9, -66.0), (63.8, -66.0), ..., (18.0, -66.0) 
        (64.0, -66.1), (63.9, -66.1), (63.8, -66.1), ..., (18.0, -66.1)
        .
        .
        .
        (64.0, -124.0), (63.9, -124.0), (63.8, -124.0), ..., (18.0, -124.0)
    ]

#thread
Yelp API 호출

    각주마다 500번의 쿼리 (limit제한때문에)
    $Select option - 'restaurant' or 'food' ?
    
    
필요사항

    python version 2.6 over
    sudo easy_install oauth2
    sudo easy_install simplejson

Output 

    Log
    
        주[\t]쿼리순번
        ny  0
        .
        .
        .
        hi 499
        
    Json
    
        주.json
        ny.json
        .
        .
        .
        hi.json
