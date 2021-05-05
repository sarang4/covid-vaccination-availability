# Covid Vaccination Availability
Small script which provides quick updates regarding vaccination availability as per your state.

## Installation

Need requests package to run the this

```bash
pip install requests
```

## Usage

```
python vacination.py -h

usage: vaccine.py [-h] {states,district,availability}
positional arguments:
  {states,district,availability} Sub commands for use
    states              states list command help
    district            district list command help
    availability        Slot Availability Command

optional arguments:
  -h, --help            show this help message and exit
```

```
python vaccine.py states

Andaman and Nicobar Islands: 1
Andhra Pradesh: 2
Arunachal Pradesh: 3
Assam: 4
Bihar: 5
Chandigarh: 6
Chhattisgarh: 7
Dadra and Nagar Haveli: 8
Daman and Diu: 37
Delhi: 9
Goa: 10
Gujarat: 11
Haryana: 12
Himachal Pradesh: 13
Jammu and Kashmir: 14
Jharkhand: 15
Karnataka: 16
Kerala: 17
Ladakh: 18
Lakshadweep: 19
Madhya Pradesh: 20
Maharashtra: 21
Manipur: 22
Meghalaya: 23
Mizoram: 24
Nagaland: 25
Odisha: 26
Puducherry: 27
Punjab: 28
Rajasthan: 29
Sikkim: 30
Tamil Nadu: 31
Telangana: 32
Tripura: 33
Uttar Pradesh: 34
Uttarakhand: 35
West Bengal: 36
```

```
python vaccine.py district

usage: vaccine.py district [-h] -s STATE_ID
vaccine.py district: error: argument -s/--state_id is required
```

```
python vaccine.py district -s 21
Ahmednagar: 391
Akola: 364
Amravati: 366
Aurangabad : 397
Beed: 384
Bhandara: 370
Buldhana: 367
Chandrapur: 380
Dhule: 388
Gadchiroli: 379
Gondia: 378
Hingoli: 386
Jalgaon: 390
Jalna: 396
Kolhapur: 371
Latur: 383
Mumbai: 395
Nagpur: 365
Nanded: 382
Nandurbar: 387
Nashik: 389
Osmanabad: 381
Palghar: 394
Parbhani: 385
Pune: 363
Raigad: 393
Ratnagiri: 372
Sangli: 373
Satara: 376
Sindhudurg: 374
Solapur: 375
Thane: 392
Wardha: 377
Washim: 369
Yavatmal: 368
```

```
python vaccine.py availability -h
usage: vaccine.py availability [-h] -d DISTRICT_ID

optional arguments:
  -h, --help            show this help message and exit
  -d DISTRICT_ID, --district_id DISTRICT_ID
                        Need district id
```
```
python vaccine.py availability -d 363

<Response [200]>
Not Available...
Sleeping....
<Response [200]>
Not Available...
Sleeping....
<Response [200]>
Not Available...
Sleeping....
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
