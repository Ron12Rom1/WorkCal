
import os
import base64

file_data = [('assets/Googel/credentials.json', 'eyJpbnN0YWxsZWQiOnsiY2xpZW50X2lkIjoiODEyNzIwNzc0NzM0LWRnNzZsdGNvZTdoMzlhZ2lhMGFnZ2RiamhybGJpazUxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwicHJvamVjdF9pZCI6IndvcmtjYWwtNDMyNTIxIiwiYXV0aF91cmkiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvYXV0aCIsInRva2VuX3VyaSI6Imh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwiYXV0aF9wcm92aWRlcl94NTA5X2NlcnRfdXJsIjoiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vb2F1dGgyL3YxL2NlcnRzIiwiY2xpZW50X3NlY3JldCI6IkdPQ1NQWC13cFVfcGk2UTVKSDk2MHMzd0JiT2N6ZnNTYzQzIiwicmVkaXJlY3RfdXJpcyI6WyJodHRwOi8vbG9jYWxob3N0Il0sICJjbGllbnRfZW1haWwiOiAiYW5vdGhlci5yb25yb25icnVrQGdtYWlsLmNvbSJ9fQ=='), ('assets/Googel/Googel_api.py', 'aW1wb3J0IGRhdGV0aW1lDQppbXBvcnQgb3MucGF0aA0KZnJvbSBnb29nbGUuYXV0aC50cmFuc3BvcnQucmVxdWVzdHMgaW1wb3J0IFJlcXVlc3QNCmZyb20gZ29vZ2xlLm9hdXRoMi5jcmVkZW50aWFscyBpbXBvcnQgQ3JlZGVudGlhbHMNCmZyb20gZ29vZ2xlX2F1dGhfb2F1dGhsaWIuZmxvdyBpbXBvcnQgSW5zdGFsbGVkQXBwRmxvdw0KZnJvbSBnb29nbGVhcGljbGllbnQuZGlzY292ZXJ5IGltcG9ydCBidWlsZA0KZnJvbSBnb29nbGVhcGljbGllbnQuZXJyb3JzIGltcG9ydCBIdHRwRXJyb3INCg0KIyBTY29wZXMgZGVmaW5lIHRoZSBhY2Nlc3MgbGV2ZWxzIHlvdXIgYXBwbGljYXRpb24gbmVlZHMNClNDT1BFUyA9IFsnaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vYXV0aC9jYWxlbmRhciddDQoNCmRlZiBpZl9jcmVkc19ub3RfdmFsaWQoY3JlZHMpOg0KICAgIGlmIGNyZWRzIGFuZCBjcmVkcy5leHBpcmVkIGFuZCBjcmVkcy5yZWZyZXNoX3Rva2VuOg0KICAgICAgICAgICAgY3JlZHMucmVmcmVzaChSZXF1ZXN0KCkpDQogICAgZWxzZToNCiAgICAgICAgZmxvdyA9IEluc3RhbGxlZEFwcEZsb3cuZnJvbV9jbGllbnRfc2VjcmV0c19maWxlKCdhc3NldHNcR29vZ2Vsc1xjcmVkZW50aWFscy5qc29uJywgU0NPUEVTKQ0KICAgICAgICBjcmVkcyA9IGZsb3cucnVuX2xvY2FsX3NlcnZlcihwb3J0PTApDQogICAgIyBTYXZlIHRoZSBjcmVkZW50aWFscyBmb3IgdGhlIG5leHQgcnVuDQogICAgd2l0aCBvcGVuKCdhc3NldHMvR29vZ2Vscy90b2tlbi5qc29uJywgJ3cnKSBhcyB0b2tlbjoNCiAgICAgICAgdG9rZW4ud3JpdGUoY3JlZHMudG9fanNvbigpKQ0KDQogICAgcmV0dXJuIChmbG93LCBjcmVkcykNCiAgICAgICAgDQpkZWYgZ2V0X2NyZWRlbnRpYWxzKCk6DQogICAgIiIiR2V0IHZhbGlkIHVzZXIgY3JlZGVudGlhbHMgZnJvbSBzdG9yYWdlIG9yIHJ1biB0aGUgT0F1dGggZmxvdyB0byBnZXQgbmV3IGNyZWRlbnRpYWxzLiIiIg0KICAgIGNyZWRzID0gTm9uZQ0KICAgICMgVG9rZW4gZmlsZSBzdG9yZXMgdXNlciBhY2Nlc3MgYW5kIHJlZnJlc2ggdG9rZW5zDQogICAgaWYgb3MucGF0aC5leGlzdHMoJ2Fzc2V0cy9Hb29nZWxzL3Rva2VuLmpzb24nKToNCiAgICAgICAgY3JlZHMgPSBDcmVkZW50aWFscy5mcm9tX2F1dGhvcml6ZWRfdXNlcl9maWxlKCdhc3NldHMvR29vZ2Vscy90b2tlbi5qc29uJywgU0NPUEVTKQ0KICAgICMgSWYgbm8gdmFsaWQgY3JlZGVudGlhbHMsIHJ1biB0aGUgT0F1dGggZmxvdw0KICAgIGlmIG5vdCBjcmVkcyBvciBub3QgY3JlZHMudmFsaWQ6DQogICAgICAgIGZsb3csIGNyZWRzID0gaWZfY3JlZHNfbm90X3ZhbGlkKGNyZWRzKQ0KICAgIHJldHVybiBjcmVkcw0KDQoNCmRlZiBsaXN0X3VwY29taW5nX2V2ZW50cyhzZXJ2aWNlKToNCiAgICAiIiJGZXRjaCBhbmQgcHJpbnQgdGhlIG5leHQgMTAgZXZlbnRzIGZyb20gdGhlIHVzZXIncyBwcmltYXJ5IGNhbGVuZGFyIHRoYXQgaGF2ZSB0aGUgbmFtZSAnQmV6ZWsnLiIiIg0KICAgIG5vdyA9IGRhdGV0aW1lLmRhdGV0aW1lLnV0Y25vdygpLmlzb2Zvcm1hdCgpICsgJ1onICAjIFVUQyB0aW1lDQogICAgdHJ5Og0KICAgICAgICBldmVudHNfcmVzdWx0ID0gc2VydmljZS5ldmVudHMoKS5saXN0KA0KICAgICAgICAgICAgY2FsZW5kYXJJZD0ncHJpbWFyeScsDQogICAgICAgICAgICB0aW1lTWluPW5vdywNCiAgICAgICAgICAgIG1heFJlc3VsdHM9MTAsDQogICAgICAgICAgICBzaW5nbGVFdmVudHM9VHJ1ZSwNCiAgICAgICAgICAgIG9yZGVyQnk9J3N0YXJ0VGltZScNCiAgICAgICAgKS5leGVjdXRlKCkNCiAgICAgICAgZXZlbnRzID0gZXZlbnRzX3Jlc3VsdC5nZXQoJ2l0ZW1zJywgW10pDQogICAgICAgIGlmIG5vdCBldmVudHM6DQogICAgICAgICAgICBwcmludCgnTm8gdXBjb21pbmcgZXZlbnRzIGZvdW5kLicpDQogICAgICAgICAgICByZXR1cm4NCiAgICAgICAgIyBGaWx0ZXIgYW5kIHByaW50IG9ubHkgZXZlbnRzIHdpdGggdGhlIG5hbWUgJ0JlemVrJw0KICAgICAgICBmb3IgZXZlbnQgaW4gZXZlbnRzOg0KICAgICAgICAgICAgc3VtbWFyeSA9IGV2ZW50LmdldCgnc3VtbWFyeScsICcnKQ0KICAgICAgICAgICAgaWYgc3VtbWFyeSA9PSAnQmV6ZWsnOg0KICAgICAgICAgICAgICAgIHN0YXJ0ID0gZXZlbnRbJ3N0YXJ0J10uZ2V0KCdkYXRlVGltZScsIGV2ZW50WydzdGFydCddLmdldCgndGltZScpKQ0KICAgICAgICAgICAgICAgIHByaW50KHN0YXJ0LCBzdW1tYXJ5KQ0KICAgIGV4Y2VwdCBIdHRwRXJyb3IgYXMgZXJyb3I6DQogICAgICAgIHByaW50KGYnQW4gZXJyb3Igb2NjdXJyZWQ6IHtlcnJvcn0nKQ0KDQpkZWYgY3JlYXRlX2V2ZW50KHNlcnZpY2UsIHN1bW1hcnksIHN0YXJ0X3RpbWUsIGVuZF90aW1lKToNCiAgICAiIiJDcmVhdGUgYSBuZXcgZXZlbnQgaW4gdGhlIHVzZXIncyBwcmltYXJ5IGNhbGVuZGFyLiIiIg0KICAgIGV2ZW50ID0gew0KICAgICAgICAnc3VtbWFyeSc6IHN1bW1hcnksDQogICAgICAgICdzdGFydCc6IHsNCiAgICAgICAgICAgICdkYXRlVGltZSc6IHN0YXJ0X3RpbWUsDQogICAgICAgICAgICAndGltZVpvbmUnOiAnVVRDJywNCiAgICAgICAgfSwNCiAgICAgICAgJ2VuZCc6IHsNCiAgICAgICAgICAgICdkYXRlVGltZSc6IGVuZF90aW1lLA0KICAgICAgICAgICAgJ3RpbWVab25lJzogJ1VUQycsDQogICAgICAgIH0sDQogICAgfQ0KICAgIHRyeToNCiAgICAgICAgZXZlbnRfcmVzdWx0ID0gc2VydmljZS5ldmVudHMoKS5pbnNlcnQoDQogICAgICAgICAgICBjYWxlbmRhcklkPSdwcmltYXJ5JywNCiAgICAgICAgICAgIGJvZHk9ZXZlbnQNCiAgICAgICAgKS5leGVjdXRlKCkNCiAgICAgICAgcHJpbnQoZiJFdmVudCBjcmVhdGVkOiB7ZXZlbnRfcmVzdWx0LmdldCgnaHRtbExpbmsnKX0iKQ0KICAgIGV4Y2VwdCBIdHRwRXJyb3IgYXMgZXJyb3I6DQogICAgICAgIHByaW50KGYnQW4gZXJyb3Igb2NjdXJyZWQ6IHtlcnJvcn0nKQ0KDQpkZWYgbWFpbigpOg0KICAgICIiIk1haW4gZnVuY3Rpb24gdG8gYXV0aGVudGljYXRlLCBsaXN0IHVwY29taW5nIGV2ZW50cywgYW5kIGNyZWF0ZSBhIG5ldyBldmVudC4iIiINCiAgICBjcmVkcyA9IGdldF9jcmVkZW50aWFscygpDQogICAgc2VydmljZSA9IGJ1aWxkKCdjYWxlbmRhcicsICd2MycsIGNyZWRlbnRpYWxzPWNyZWRzKQ0KICAgIA0KICAgICMgTGlzdCB1cGNvbWluZyBldmVudHMNCiAgICBwcmludCgiTGlzdGluZyB1cGNvbWluZyBldmVudHM6IikNCiAgICBsaXN0X3VwY29taW5nX2V2ZW50cyhzZXJ2aWNlKQ0KDQogICAgIyBDcmVhdGUgYSBuZXcgZXZlbnQNCiAgICBwcmludCgiXG5DcmVhdGluZyBhIG5ldyBldmVudDoiKQ0KICAgIHN1bW1hcnkgPSAiU2FtcGxlIEV2ZW50Ig0KICAgIHN0YXJ0X3RpbWUgPSAnMjAyNC0wOC0xNlQxMDowMDowMFonICAjIENoYW5nZSB0byB5b3VyIGRlc2lyZWQgc3RhcnQgdGltZQ0KICAgIGVuZF90aW1lID0gJzIwMjQtMDgtMTZUMTE6MDA6MDBaJyAgICAjIENoYW5nZSB0byB5b3VyIGRlc2lyZWQgZW5kIHRpbWUNCiAgICBjcmVhdGVfZXZlbnQoc2VydmljZSwgc3VtbWFyeSwgc3RhcnRfdGltZSwgZW5kX3RpbWUpDQoNCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6DQogICAgbWFpbigpDQo='), ('assets/images/button_1.png', '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'), ('assets/images/button_2.png', 'iVBORw0KGgoAAAANSUhEUgAAAFEAAAAaCAYAAADPELCZAAAL2ElEQVR4nO2ZaZRV1ZXHf+fc+4b7Xo0CxQwCLiyQQcEIElqMGFmYhm6BOHQTaVlKotCx4xhBBc1SE4MgLRhJD9Gl0LoM8xQDcQQZFJUKQ1EWiMVYxVT16s33nnP6w331oIBCkxXbjiv7S6319rnn7P0/e/jvUwKmS3hM9+k2Zbwl7SnGuJciRIi/SQtiUkLYW4325lXsnfcqIARAv+6TH5VW8DFjDMZ4X7OR//9FChuEQKvs9Iq98x4X/XrceZOU4Ve1drUBI8D6uo38KxAFCCkD0njeeGmM9RPQBgx/A/BLiwUGY7TRUt9vI+irtRJNqf1NESkFQgi01hjzVZwgpDEKYSi3BURaXgcCH1tzDkuEaFn3dYoxhlTKxXUVkUgQaUn4qkwUImSfT6+VQSkPIQSBoI3RpyzR2qCUAsC2ZR7Qv4xdAiFAKfMn54cxEAzaXFzeka7dytj8fhUnT8axbfkVRSScG0ThA1hQGKaoOEI67VJ3pJ5wOIDWBmMMjhOkpDQKwMkTcTIZ9y8CpBCCbNbFczWRqM+0vmykSymJx1MMGtKXF16cjGVJxl7/JEePNhAIWF9Zxshz/WjljLl2xKUsX/sIS9ZM5Zpr+xJrSBIM2iTiGb49rDfL1z3K0t8/Qs9eHcmkXaT0QZSWxLIkUvp/TwfXsiS2bWFZp44WQmDbkkDAIpNx6dWnMzPnTuQ/X/lX2rYrwRiw7fP3PCt3piUlwaCNZUmyWQ+dyx7/DCtnl8ivP9MuKZtDYtn+70K2HCDnTWfbtgiFAoRCAZ6cNYH9+49TvfsQluU7HQ4HfNCaDhC+sfFYCk8pbMvC8xSRaIhg0EZrQ319As9TBAM2BYUOAJ6nqD+ZQkqB8gwXl3dk9JhBaGOINSQ5djRG2AlSUBA+K72FjxCxhiTGQGMsSWNjKg9cTk0269HYmMKSEsuWeJ7CsiQFBQ7GnLIrFAoQjYYwxs+AE8fjGK1xIiHC4eA5o/m8IPrk23eyuCTK03NuY8KNs6ira8jpyd80gNGQSmUYPqI/Vw4tp6AgTM3nR1m59AP21xwjGg3xT7cOo6xtMfs+q+P3qz/GGGjXvoQJtw/HcYIsePFtEokMSmlcV/HP/3I18cYUqWSWFUu34HmqWWRrY3CzHiNHX86Ay3uQTmUJOQGM8eupEAI3q+jWqx1XD+9L+w4X4ESCJOJptmys4s21FYTDAW4ZfxXtO5ayo6KG997ZiZSSsBPk5h8Mo6AgzMb1lXy8dQ+OE2zm8xeC2HSLAoPnKcp7d2La4zcx6da5+eLf5I9fyzzumzqWO+66rtkeN9w4hCm3v8D2bfsoLony4/tGo7XmtqNzWPfGJ8x8biIjRw1ke8Xn/PvMFQQCVj7dptzz9/l93lj9Ea7rIaXAGD8DUimXBx4ex8QfXntO+6UUZNIuvS7pzAMPj22mm3D7cH75xCLmzlrFqBsGMXjoxVTtOsjGDZUk4hkGXdmTqTO+D8CuHfvxPJ27wOYgnrMmnimJZJZ5z64incoyeswgvn/LUOrrE3m9ZVk0xpJcP2ogd9x1HZ6nmD93DXf/6NdUVR7kwm5l3H3/KMJOkPlz17Bs0WaklEy+53vcfud1jBw1kCOHT/JvP/oPkol0vi65ruL1hev57/lrmffsKtxcFBrj17B4PM2VQ8vzAL731g5mPLSAP7yxDTiVKaFwgKrKg8ydvYqH7nmJH0+azztvbscYuG3Sd3EiQZa8vhGtDV26lXFRzw4kEmn6D+yGUppPdx9i04bdOE4QpfVZ+HxhJAJEoyGWL96M52nu/ek/8uCjY3n9fzagtZ8yWhsCQZuRoy/HGMOHW6r5za/XEWtIUloaZdrjN3HZwB6UlRVTW9vAzCcXM+DyHlwxuCdXDO6J5yl++cRiavbVES0Io3OGuq5i9tPLqNl3lLATJBINnVbnBJ6rGDrsEowx1B6u58GfvMjO7TXs+6yO4SP654A0BIM2lTsPsKfqMBf2aIsUgrfWVjDsmj4UFjl06HABG97byckTcVq1LuTbV/Viy8YqhgzthWVJ3n+vklhDkuKSCEr9mSAabSgqjvDCnNVcPbwPA791EbfdMRxjDFJKtNaEnRBt25cihOCKwT3ZVPFMsz1atykiEg0RCtkcqDnGnJnLeHrORISAt9dVsOjVDbRpW8KJ4435b4SAkpII8VYFBII2nqvyOqU0oXCADh39Mz+tOkQikaZDx1ZEouH8OiklyVSWcTcP4cFHxtGmrPgM5yAUCrCn+jDr39nJ6DGDGDyknJ7lH9K3f1fAt09af2Z3zp9jfNqjlGLGQwtZuOR+SkoLTjkLaK3xPIUxsLf6CG+tqyAaDecLv1KaeGMarQ2FRQ6jxwzKd/UB37qIocN688GWaqxcKjc1wXTaxXU1GK8ZzfDJuN98jDEUl0TQypBJu/lIlgKyWZdOnVvxs1+Mx4mEePftHaxa9gGXDezOzeOv8psnfmSvXLqFfxg7iF59OjNp8ggCQZvq3Yf4+KO9RCLBc0YhfIma6Hdog1KaSDTMjj/W8Pyc1ZADzhiDtCTJRIbq3YcQAsLhACuWbOahe19i+gOvMHfWSuY8vYxYLEUqleWHU0Zy1Xf6sOOPNSx6bQMXtCrk8V+Mp1WrAlzPI5VyEcKfPPr2vxClFAVF4WZ2CSlwsx7VVYcRQlDeuxOjx1yB63lYucZjADfr0aVra5xICKU0v5m/lmeeXcLyxZt937RBa020IMym9ZV8snUvJaVRbrhxCACrV2wlVp/EslrmqecF0e/APkkVApSnKC6O8vJ/vcknH+1FylNE2rIlC196h2zWo1OX1ixf+yhr1/+MlW9OZ1PFTH4w8Rrqauv5u2G9mTRlBEYbnnlqCdN/upCaz4/S/aJ2fvc0ULljP7GGJJYleWrWrSxZM5VFq6fRrn0pruuPof5E5bD0t5s4UHOcYDDAEzNv5XdvP8b908YhhM9zw06QPdVHqK9P5PabwKqV03ng4XEIIQhFggjhk+902mXRa+/7/liSxsYUa1Z8mJ/U/mQQfX7lkYinicWSKOWHvZSCTMZl9s+XEWtI0hhL4boekUiIXTv2c9fE5/lk615cV9GzvCO9+nT2uabr4ThB7rz7etysYulvN7FxfSXpVJbnn11NY2OK73y3H8OG9+HT3YeYMXUhtYdPEnZCXNKvKyWlUUoviKJz87QxhkDAou5IPZMmPMeGd3eRybj07tuFC7uXkU677Pn0MJm0S11tjIfve5nP9tZS1raEEd8bwKUDupFMZti96yDpdJZsxsO2JcsXb2Z/zVGkFPzhd9uoqjxI2Dk3yc5j1a/HlHNqjfE7bigUAOOT6NNHKM9TFBY5SCFIJrMo5U8A8cY0kWiIbj3a0bpNIclEhoMHTlB/ohFpS79OKk0ymUFr/1K01hQUOghAaU0qmSWdytK6rIjOXdoghODggePE6hNnPcZIKUjnRs4uXdvQqk0RytMcPxbj+LHGHK+UpFNZCgrDtO/YiqIiBzfrUVvbQLwxRTbr0rFTazxPcdnAHsx46hacSJAJN85m88YqotHQeSOxRRCbgGz62E/d5pHqeeosnbQkWmkyGRelNFII7ICVn32bJo7T51bwm4QxBikEMjffuq7CdRVgsG2rxfnZJ9+GbMbDUxohfO5qWzLfjKQUeJ7Gc5XfeIQgYEuE9M9asOg+evftnOeory14l2n3vkxhkXNeAAFsjMm09I+ppoeBJkDPBLjJqdN1OtfBHCeI37dNfg4FCAQsQJy135l7ae3v76+n2R5nSpOTwVCAkCC/vunspjWWJbDsAKeTFaU0ti2pq22gXYdSEvE0697Yxq/mrMKJBL/w+cxAUvTtPuVjKa3+xngGxJeaYL5p0nQ5YSeIVoaG+gRhJ4Blne/5zGgpbKGM2iKNETOFkCL3HqJa+OIbLU0sJJXMkMm4FBQ65wXQgPLxkkKgZsvtnz23QKvsdCkDUooveLT7hov/6CHy/LclkcK2pAxIrTMzKvb86jVBrnD16z75ZiHkZIMeCML5P7P8r05MRgp7m0E9t6167iswXf4vfK+YRsW/8ocAAAAASUVORK5CYII='), ('assets/images/button_3.png', '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'), ('assets/images/button_4.png', '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'), ('assets/images/entry_1.png', 'iVBORw0KGgoAAAANSUhEUgAAAIIAAAAZCAYAAAD9ovZ9AAACTUlEQVR4nO3bwWsVVxTH8c+5L6AWS+hWKdgsCpYKpRUUFwpu3KcWXHVTsZvi31Khm3bbZds/oAsDuhCzUISKiIuIIC6VYIkJJO90cd9NXkPtLom+uV8YeMMwjwu/H3PPnPObsIvMLBExnvz+EF/jIs7gYxzZfU/nnWQDK7iHW/gtIlb5t8aNmD7JzFFEbGXmB7iO73FiP1bd2XOe4Cf8EhEbTet2cdsIUyb4HL/ii3YJYxS7jNN552nahaofLONqRDycNkOw86jIzIv4HR9hEyNd/FlhPDnm8AqXI2KpaR9TJvgMdzCPLdUEndljUzXDKs5FxKPMLJGZBYdxG1/pJhgCTeO/cBZvWvX4nWqCth10ZpuRqvUpXI+IjMycx318ohYX5X/+oDM7tCLyBU4WfIMF3QRDo6iaH8diUZtFOTk6w6Lpfqmo/YLp98zOcGi9odORmes4dMAL6hwsa5GZfUvoKFg76EV0DpyNgueTk/5kGB5N85WijinbcKIzLMaq9g8K/lQrxz5cGh5N96XIzKN4jGN6U2lItM7iU3xZIuJvNbAQ+vYwJJoRfoyI1cjMUONnd9UhRJ8+zj5N43s4j/WCiIg1XFFn1G0y1ZlNmglW8e1Eey2UUiLiERbxUg0ubOpbxSyRdmIGr7C4HUqJGBeYmGEUEUu4oOba5tTCcay6qPcZ3j/SjnahavoA5ycxtVFLM78txXwI1/ADPt3PlXf2jGf4GTciYu2tKebGru8a5tW8wgU1wbSgD6jeF96oXeNl3MQfEfGa//6u4R95kuBO6Dm3WAAAAABJRU5ErkJggg=='), ('assets/images/entry_2.png', 'iVBORw0KGgoAAAANSUhEUgAAAIIAAAAZCAYAAAD9ovZ9AAAB5klEQVR4nO2bv2oVQRTGf9/sFbTSNoWgoJVNsPEdJKRVc30ClQTs0uUJBAPJE4T8aYP4Djaigo1YiCCxjJVCsvulmBlXL7ay3LvnB8PCzA4MnDNnZvd8RxRsC5CkzvZlYArcB+4BS0AimEfOgRPgHfAaOJD0w3YCLMkAguwEtcP2FNgE7gyx6uC/8wnYknQAve1VI0FpL4D1MqErzzoWzC8uDfrIvgNs1LEJkCS1tneAJ8AZ0BBHwSLx52buSnsKdJLWbTf1aHgAHJLPk4aIAIuOyba+BEwl7cv2NeAtcKO8EJFgHHTkDf8ZWE7AQ+Am4QRjI5FtfhtYS8AKf18mgvFQ7b4q21+B66Uj7gbj5JtsnwGToVcSDEor23EkBHE5DDLhCAEQjhAUwhECIDtCO/QigsE5T8D3oVcRDEb9YjxJ5DyDicgwRjqy7T8k4JjQHIyVavdXsn0FeA/cIhJPY6JmH78Ad5Okn8BW6WyJ5NMYML0jbEo6TbYbSfvANlmo0NLL1ILFoyOLUibArqQj282sZvElWcJUJ0DcHxaBf2kWt4HndSwV9bIltZKeAWtkpWsqLZxg/hG9PT8CjyVtSGopkvbfRp6pa7gKPCLXNSyT6xoiVT2fdOR/RW/IdQ17kn7N1jVcAM81p+4CPpH0AAAAAElFTkSuQmCC'), ('assets/images/image_1.png', 'iVBORw0KGgoAAAANSUhEUgAAAJAAAAAlCAYAAACtQWB+AAABrUlEQVR4nO3cPWsUYRTF8XPu7M6+aBlS+9ZYCIIfRouU2UqbgLVrrAUbLSSWCvHDCIKFlbFfUrmQzc7uPMciWtgY2FvMLpzfJzjFH+Zp5nIKxTFYTvZ/HNQYPWtw+ZCIASCY/UUQRWXRZ/1lXVbvDs9vnwoiAeD9/tmLMW8et1hhrabrrbalCKLHGoEKl5pPJ7N7r3iyd/Z4WN04bbQoBUUEq66H2vYS1AaCNcexXM8PAuRRUauCAsdj1yFYFbQoWEsVn/dIPFihIXH1OTO7DhGx0hIE7wfBsR/MthkOQo7HNiZE1xNstzkgS3FAluKALMUBWYoDshQHZCkOyFIckKU4IEtxQJbigCzFAVmKA7IUB2QpDshSHJClOCBLcUCW4oAsxQFZigOyFAdkKQ7IUgLwH822GYIIQMuuh9guIiRdBKDvfQ4klNL1JNsNgkoftQR8CyBeB3oMVBDUdj3Ottuf+0AIVoT0Jg5ntz5d6Ne05ihqDiv6TWT/0eegqjmORTt/OTm/85lXd+6oD3s/n/Si/3SF5lEgRr7aYf8ihLKsMfzaYPF2Mrv7cQrFbxjUgfhpvAm7AAAAAElFTkSuQmCC'), ('assets/images/image_2.png', 'iVBORw0KGgoAAAANSUhEUgAAAIIAAAAZCAYAAAD9ovZ9AAABA0lEQVR4nO3asUlEQRSF4f/MBqLVCIKtaLAdaA2uGgsGYgcKaycmBouBlai8wHcMZrYE94J7vgoOzA+TXNlukmbbS+ASOAYOiP/sG3gDHiWtbUsAtq+Am9JpUWUl6Va2z4A1MAMGFrW7Ykd+AAENWMr2K3BKj6BVLoudm+kxbGT7EzgqHhS1Jtl29Yqol68ggIQQQ0IIICHEkBACSAgxJIQAEkIMCSGAhBBDQgggIcSQEAJICDE0YKoeEeW+GvBBv06ai8fE7m3PE98bcEc/V4J+xxb7YfvWAu6bpGdgRf8mcri6Pxb0N7+W9CLbkmTb58AFcAIclk6MvzYBG+BB0pPt9gvMf0VFSBil2QAAAABJRU5ErkJggg=='), ('assets/images/image_3.png', 'iVBORw0KGgoAAAANSUhEUgAAAJAAAAAlCAYAAACtQWB+AAABrUlEQVR4nO3cPWsUYRTF8XPu7M6+aBlS+9ZYCIIfRouU2UqbgLVrrAUbLSSWCvHDCIKFlbFfUrmQzc7uPMciWtgY2FvMLpzfJzjFH+Zp5nIKxTFYTvZ/HNQYPWtw+ZCIASCY/UUQRWXRZ/1lXVbvDs9vnwoiAeD9/tmLMW8et1hhrabrrbalCKLHGoEKl5pPJ7N7r3iyd/Z4WN04bbQoBUUEq66H2vYS1AaCNcexXM8PAuRRUauCAsdj1yFYFbQoWEsVn/dIPFihIXH1OTO7DhGx0hIE7wfBsR/MthkOQo7HNiZE1xNstzkgS3FAluKALMUBWYoDshQHZCkOyFIckKU4IEtxQJbigCzFAVmKA7IUB2QpDshSHJClOCBLcUCW4oAsxQFZigOyFAdkKQ7IUgLwH822GYIIQMuuh9guIiRdBKDvfQ4klNL1JNsNgkoftQR8CyBeB3oMVBDUdj3Ottuf+0AIVoT0Jg5ntz5d6Ne05ihqDiv6TWT/0eegqjmORTt/OTm/85lXd+6oD3s/n/Si/3SF5lEgRr7aYf8ihLKsMfzaYPF2Mrv7cQrFbxjUgfhpvAm7AAAAAElFTkSuQmCC'), ('assets/images/image_4.png', 'iVBORw0KGgoAAAANSUhEUgAAAIIAAAAZCAYAAAD9ovZ9AAABA0lEQVR4nO3asUlEQRSF4f/MBqLVCIKtaLAdaA2uGgsGYgcKaycmBouBlai8wHcMZrYE94J7vgoOzA+TXNlukmbbS+ASOAYOiP/sG3gDHiWtbUsAtq+Am9JpUWUl6Va2z4A1MAMGFrW7Ykd+AAENWMr2K3BKj6BVLoudm+kxbGT7EzgqHhS1Jtl29Yqol68ggIQQQ0IIICHEkBACSAgxJIQAEkIMCSGAhBBDQgggIcSQEAJICDE0YKoeEeW+GvBBv06ai8fE7m3PE98bcEc/V4J+xxb7YfvWAu6bpGdgRf8mcri6Pxb0N7+W9CLbkmTb58AFcAIclk6MvzYBG+BB0pPt9gvMf0VFSBil2QAAAABJRU5ErkJggg=='), ('assets/Logs/log.txt', ''), ('assets/Logs/temp.txt', 'W10NCg0')]

os.makedirs("out/assets/images/")
os.makedirs("out/assets/Googel/")
os.makedirs("out/assets/Logs/")

for asset in file_data:
    print(asset[0])
    print(".png" in asset[0])
    with open("out/" + str(asset[0]).removesuffix(".png") + ".png" if ".png" in asset[0] else "out/" + str(asset[0]).removesuffix(".py") + ".py" if ".py" in asset[0] else "out/" + str(asset[0]).removesuffix(".json") + ".json" if ".json" in asset[0] else "out/" + str(asset[0]).removesuffix(".txt") + ".txt", "wb") as out_file:
        out_file.write(base64.b64decode(asset[1]))

        
###END###
###END###
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from datetime import datetime as _dt
from datetime import timedelta
# import assets.Googel.Googel_api as Googel_api

global log
log = []


date = _dt.today()



def change_mid_text(new_text, is_error=False):
    """Updates the mid label text."""
    canvas.itemconfig((11,), text=new_text, fill="red" if is_error else "black") 
    print(f"Updated mid label text to: {new_text}")

def on_press_next():
    """move to the next day"""
    global date
    date += timedelta(days=1)
    target_text = canvas.find_withtag("target_text")  # Find the text element with the tag
    canvas.itemconfig(target_text, text=date.strftime("%a %d/%m")) 
    change_mid_text("Moved to next day")

def on_press_prev():
    """move a day back"""
    global date
    date -= timedelta(days=1)
    target_text = canvas.find_withtag("target_text")  # Find the text element with the tag
    canvas.itemconfig(target_text, text=date.strftime("%a %d/%m")) 
    canvas.itemconfig((11,), text=date.strftime("%a %d/%m")) 
    change_mid_text("Moved to previous day")

def check_input(time_start, time_end):
    if time_start == "" or time_end == "":
        change_mid_text("Please enter both start and end times", True)
        return 0
    elif not time_start.replace(":", "").isdigit() or not time_end.replace(":", "").isdigit():
        change_mid_text("Please enter only numbers", True)
        return 0
    else: return 1

def procces_time_format(time_start, time_end):
    """Processes the time format and returns the format to be entered in the database.
    in this format: (startTime, endTime).
    if there is a format or numerical value error, returns (None, None)
    and sets mid label to error message"""
    
    times = [time_start, time_end]
    times.reverse()
    to_return = [None, None]
    for i, time in enumerate(times):
        if ":" in time:
            hour, min = time.split(":")
            if int(hour) >= 0 and int(hour) <= 25:
                if int(min) >= 0 and int(min) < 60:
                    to_return[i] = time
                else:
                    """whay to do if minutes enters are invalid"""
                    change_mid_text(f"{'Start time Eroor: ' if i == 1 else 'End time eroor: '}Invalid minutes entered\n Please enter a number between 00 and 59", True)
                    to_return[i] = None
            else:
                """whay to do if hours enters are invalid"""
                change_mid_text(f"{'Start time Eroor: ' if i == 1 else 'End time eroor: '}Invalid hours are entered\n    Please enter an hour between 0 and 25", True)
                to_return[i] = None
        elif len(time) == 3 or len(time) == 4:
            hour = time[:-2]
            min = time[-2:]
            print(hour, min)
            if int(hour) >= 0 and int(hour) <= 25:
                if int(min) >= 0 and int(min) < 60:
                    to_return[i] = f"{hour[1:]}:{min}" if hour[0] == "0" else f"{hour}:{min}"
                else:
                    """whay to do if minutes enters are invalid"""
                    change_mid_text(f"{'Start time Eroor: ' if i == 1 else ' End time eroor: '}Invalid minutes entered\nPlease enter a number between 00 and 59", True)
                    to_return[i] = None
            else:
                """whay to do if hours enters are invalid"""
                change_mid_text(f"{'Start time Eroor: ' if i == 1 else 'End time eroor: '}Invalid hours are entered\n   Please enter an hour between 0 and 25", True)
                to_return[i] = None
        elif len(time) == 0:
            return (False, None)
        elif len(time) != 3 and len(time) != 4: 
            change_mid_text(f"        {'Start time Eroor: ' if i == 1 else '  End time eroor: '}Invalid time entered.\nPlease enter between 3 and 4 numbers in total", True)
            to_return[i] = None
        else:
            change_mid_text(f"{'Start time Eroor: ' if i == 1 else 'End time eroor: '}Invalid time entered. Please enter only numbers and ':' in this format: HH:MM", True)
            to_return[i] = None
    
    return to_return

def on_press_submit():
    time_start = entry_1.get()
    time_end = entry_2.get()
    check = check_input(time_start, time_end)
    if check:
        time_end_toEnter, time_start_toEnter = procces_time_format(time_start, time_end)
        if time_start_toEnter != None and time_end_toEnter != None:
            """ if evrything is OK """
            print(f"Time start: {time_start_toEnter}, Time end: {time_end_toEnter}")
            entry_1.delete(0, 999)
            entry_2.delete(0, 999)
            log.append({"day": date.strftime('%d-%m-%y'), "start_time": time_start_toEnter, "end_time": time_end_toEnter})
            on_press_next()
            change_mid_text(f"Added a new working day from: {time_start_toEnter} to: {time_end_toEnter}.\n                          Moved to next day.")
            print(log)
        else: 
            """ if there is an error """
            print("There is an error")
    else: 
        """ if there is an error """
        print("There is an error")

def update_text_on_button_click():
    """Updates the text of the target text element to 'No' when clicked."""
    target_text = canvas.find_withtag("target_text")  # Find the text element with the tag
    canvas.itemconfig(target_text, text="No") 

def add_to_google():
    """Adds the hours of the target text element to Google calendar."""
    # target_text = canvas.find_withtag("target_text")  # Find the text element with the tag
    # text = canvas.itemcget(target_text, "text")
    # print(f"Adding {text} to Google Calendar...")
    # Add your Google Calendar API code here

window = Tk()

window.title("WorkCal")
window.geometry("800x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

#Logo Banner
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    100.0,
    fill="#17153B",
    outline="")

#Logo Name
canvas.create_text(
    26.0,
    23.0,
    anchor="nw",
    text="WorkCal",
    fill="#FFFFFF",
    font=("Ubuntu Bold", 48 * -1)
)

#Date
canvas.create_text(
    400.0,
    150.0,
    anchor="center",
    text=date.strftime("%a %d/%m"),  # Replace with the text variable if needed
    fill="#000000",
    font=("Ubuntu Bold", 48 * -1),
    tag="target_text",  # Assign a unique tag for easy reference
)

#From
canvas.create_text(
    285.0,
    208.0,
    anchor="nw",
    text="From:",
    fill="#000000",
    font=("Ubuntu Bold", 28 * -1)
)

#To
canvas.create_text(
    304.0,
    254.0,
    anchor="nw",
    text="To:",
    fill="#000000",
    font=("Ubuntu Bold", 28 * -1)
)

#Purpule rec, enter 1
image_image_1 = PhotoImage(
    file="assets/images/image_1.png")
image_1 = canvas.create_image(
    444.0,
    226.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file="assets/images/image_2.png")
image_2 = canvas.create_image(
    444.0,
    226.0,
    image=image_image_2
)


entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    font=("Ubuntu Regular", 24 * -1),
    highlightthickness=0
)
entry_1.place(
    x=385.5,
    y=214.0,
    width=105.0,
    height=22.0
)

#purple rec, enter 2
image_image_3 = PhotoImage(
    file="assets/images/image_3.png")
image_3 = canvas.create_image(
    444.0,
    269.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file="assets/images/image_4.png")
image_4 = canvas.create_image(
    444.0,
    269.0,
    image=image_image_4
)

entry_image_2 = PhotoImage(
    file="assets/images/entry_2.png")
entry_bg_2 = canvas.create_image(
    444.0,
    268.5,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    font=("Ubuntu Regular", 24 * -1),
    highlightthickness=0
)
entry_2.place(
    x=385.5,
    y=258.0,
    width=105.0,
    height=22.0
)

#Mid label
canvas.create_text(
    400.0,
    320.0,
    anchor="center",
    text="",
    fill="#000000",
    tag="mid_text",
    font=("Ubuntu Bold", 26 * -1)
)

button_image_1 = PhotoImage(
    file="assets/images/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_1 clicked"), canvas.itemconfig((11,), text=""), on_press_submit()],
    relief="flat"
)
button_1.place(
    x=345.0,
    y=366.0,
    width=110.0,
    height=30.55555534362793
)

button_image_2 = PhotoImage(
    file="assets/images/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_2 clicked"), canvas.itemconfig((11,), text=""), on_press_next(), entry_1.delete(0, 999), entry_2.delete(0, 999)],
    relief="flat"
)
button_2.place(
    x=428.0,
    y=410.0,
    width=81.0,
    height=26.0
)

button_image_3 = PhotoImage(
    file="assets/images/button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_3 clicked"), canvas.itemconfig((11,), text=""), on_press_prev(), entry_1.delete(0, 999), entry_2.delete(0, 999)],
    relief="flat"
)
button_3.place(
    x=287.0,
    y=410.0,
    width=110.0,
    height=26.0
)

button_image_4 = PhotoImage(
    file="assets/images/button_4.png")
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: [print("button_4 clicked"), canvas.itemconfig((11,), text="")],
    relief="flat",
)
button_4.place(
    x=366.0,
    y=451.0,
    width=68.0,
    height=24.0,
)

window.resizable(False, False)
window.mainloop()


temp_logs = open("assets/Logs/temp.txt", "w")
temp_logs.write(str(log) + "\n\n")
for i, entry in enumerate(log):
    temp_logs.write(f"Entry {i}:\n")
    temp_logs.write(f'Date: {entry["day"]}\nStart time: {entry["start_time"]}\nEnd time: {entry["end_time"]}')
    temp_logs.write("\n================================\n")
print("Successfully added to info temp database")

add_to_google()

temp_logs.close()









