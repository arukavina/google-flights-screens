# Google Flights Screenshot taker

This simple script takes screenshots of GF's results for a given search

## URL Template used:

```python
base_url = 'https://www.google.com/flights?hl=en-US#flt={0}.{1}.{2}*{1}.{0}.{3};c:{4};e:1;sd:1;t:f'
url = base_url.format(from_place, to_place, from_date, to_date, currency)
```


___

### Contact

Andrei Rukavina - [rukavina.andrei@gmail.com](mailto:rukavina.andrei@gmail.com)