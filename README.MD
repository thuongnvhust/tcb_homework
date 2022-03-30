

## Calculate percentile
In case of number of elements less than 100, I calculate percentile by sorting array (merge-sort) then use percentile rank.

Otherwise, if number of elements equal or more than 100, I use numpy - a well-known library for scientific computing.

## Storage
Save pool in a file on disk (resource/pools.json) with format like below
```
{
    "123547": [
        1,
        2,
        6,
        7,
        7
    ],
    "123546": [
        1,
        7,
        6
    ]
}
```

## Run

Install requirements
> pip install -r requirements.txt

Run webservice in port 8080
> python main.py --port 8080 --debug False