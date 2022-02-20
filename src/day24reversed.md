# MONAD Reverse Engineered

## Summary

On line 79 of the MONAD code below variable

```
z =
r4/26 =
(r3*26+i4+16)/26 =
((r2*26+i3+2)*26+i4+16)/26 =
(((r1*26+i2+10)*26+i3+2)*26+i4+16)/26 =
((((i1+15)*26+i2+10)*26+i3+2)*26+i4+16)/26
```

where i1, i2, i3, and i4 are input values.

We notice a pattern, which repeats from the line 79 onward, that z is
multiplied and then divided by 26. The division by 26 is the only way z ever
decreases (all the input values i are positive). Thus, z can be 0 in the end
only if z is divided by 26 at least one time more than it is multiplied by it.

On lines 79, 115, 169, 187, 205, 223, 241, and 252 the execution branches
depending on the values of w, which holds the input values, and x. By counting
the times when z is multiplied or divided by 26, we notice that z can be 0 in
the end only if w equals x on every branch point.

It depends on the following conditions whether w equals x:

```
line 79, i4+4 = i5
line 115, i6+2 = i7
line 169, i9-8 = i10
line 187, i8+5 = i11
line 205, i3 = i12
line 223, i2-6 = i13
line 241, i1+1 = i14
```

Supposing the conditions hold on every branch point, z equals the following:

```
line 79, z1 = ((((i1+15)*26+i2+10)*26+i3+2)*26+i4+16)/26
line 115, z2 = (z1*26+i6+11)/26
line 169, z3 = ((z2*26+i8+16)*26+i9+6)/26
line 187, z4 = z3/26
line 205, z5 = z4/26
line 223, z6 = z5/26
line 241, z7 = z6/26
line 252, z8 = z7
```

The largest model number satisfying the conditions above is

```
i 1 2 3 4 5 6 7 8 9 10 11 12 13 14
  8 9 9 5 9 7 9 4 9  1  9  9  3  9
```

where i1 - i14 are the input values.

The smallest model number satisfying the conditions above is

```
i 1 2 3 4 5 6 7 8 9 10 11 12 13 14
  1 7 1 1 5 1 3 1 9  1  6  1  1  2
```

## Details

The details follow.

```
                w       x       y       z       notes
                -------------------------------------
                0       0       0       0       start values
    
1   inp w       i1      0       0       0       1. input
2   mul x 0             0
3   add x z             0
4   mod x 26            0
5   div z 1                             0
6   add x 15            15
7   eql x w             0                       x=15, 0 < w < 10
8   eql x 0             1
9   mul y 0                     0
10  add y 25                    25
11  mul y x                     25
12  add y 1                     26
13  mul z y                             0
14  mul y 0                     0
15  add y w                     i1
16  add y 15                    i1+15
17  mul y x                     i1+15
18  add z y                             i1+15
-----------------------------------------------------
                w       x       y       z       notes
                i1      1       i1+15   i1+15
                                        r1      denote z=r1 (result 1)
    
19  inp w       i2                              2. input
20  mul x 0             0
21  add x z             r1
22  mod x 26            r1mod26
23  div z 1                             r1
24  add x 15            r1mod26+15
25  eql x w             0                       x>10, 0 < w < 10
26  eql x 0             1
27  mul y 0                     0
28  add y 25                    25
29  mul y x                     25
30  add y 1                     26
31  mul z y                             r1*26
32  mul y 0                     0
33  add y w                     i2
34  add y 10                    i2+10
35  mul y x                     i2+10
36  add z y                             r1*26+i2+10
-----------------------------------------------------
                w       x       y       z       notes
                i2      1       i2+10   r1*26+i2+10
                                        r2      denote z=r2 (result 2)
    
37  inp w       i3                              3. input
38  mul x 0             0
39  add x z             r2
40  mod x 26            r2mod26
41  div z 1                             r2
42  add x 12            r2mod26+12
43  eql x w             0                       x>10, 0 < w < 10
44  eql x 0             1
45  mul y 0                     0
46  add y 25                    25
47  mul y x                     25
48  add y 1                     26
49  mul z y                             r2*26
50  mul y 0                     0
51  add y w                     i3
52  add y 2                     i3+2
53  mul y x                     i3+2
54  add z y                             r2*26+i3+2
-----------------------------------------------------
                w       x       y       z       notes
                i3      1       i3+2    r2*26+i3+2
                                        r3      denote z=r3 (result 3)
    
55  inp w       i4                              4. input
56  mul x 0             0
57  add x z             r3
58  mod x 26            r3mod26
59  div z 1                             r3
60  add x 13            r3mod26+13
61  eql x w             0                       x>10, 0 < w < 10
62  eql x 0             1
63  mul y 0                     0
64  add y 25                    25
65  mul y x                     25
66  add y 1                     26
67  mul z y                             r3*26
68  mul y 0                     0
69  add y w                     i4
70  add y 16                    i4+16
71  mul y x                     i4+16
72  add z y                             r3*26+i4+16
-----------------------------------------------------
                w       x       y       z       notes
                i4      1       i4+16   r3*26+i4+16
                                        r4      denote z=r4 (result 4)
    
73  inp w       i5                              5. input
74  mul x 0             0
75  add x z             r4
76  mod x 26            r4mod26
77  div z 26                            r4/26
78  add x -12           r4mod26-12

On line 79, x = 1 if r4mod26-12 == i5, and x = 0 otherwise.

Now,
r4mod26-12 =
(r3*26+i4+16)mod26-12 =
((r2*26+i3+2)*26+i4+16)mod26-12 =
(((r1*26+i2+10)*26+i3+2)*26+i4+16)mod26-12 =
((((i1+15)*26+i2+10)*26+i3+2)*26+i4+16)mod26-12.

By congruence, the previous line equals (i4+16)mod26-12. Because 0 < i4 < 10,
this is reduced to i4+16-12 = i4+4. Thus, on line 79 x = 1 if i4+4 == i5,
otherwise x = 0.

Now, z = z1 = r4/26 = ((((i1+15)*26+i2+10)*26+i3+2)*26+i4+16)/26.
-------------------------------------------------------------------------------------
                        i4+4 == i5             |        i4+4 != i5
                w       x       y       z      |w       x       y       z       notes
                i5              i4+16   r4/26  |i5              i4+16   r4/26

79  eql x w             1                               0
80  eql x 0             0                               1
81  mul y 0                     0                               0
82  add y 25                    25                              25
83  mul y x                     0                               25
84  add y 1                     1                               26
85  mul z y                             r4/26                           r4/26*26
86  mul y 0                     0                               0
87  add y w                     i5                              i5
88  add y 12                    i5+12                           i5+12
89  mul y x                     0                               i5+12
90  add z y                             r4/26                           r4/26*26+i5+12
-------------------------------------------------------------------------------------
                w       x       y       z      |w       x       y       z       notes
                i5      0       0       r4/26  |i5      1       i5+12   r4/26*26+i5+12
                                        r5                              r5      denote z=r5 (result 5)

91  inp w       i6                              i6                              6. input
92  mul x 0             0                               0
93  add x z             r5                              r5
94  mod x 26            r5mod26                         r5mod26
95  div z 1                             r5                              r5
96  add x 10            r5mod26+10                      r5mod26+10
97  eql x w             0                               0                       x>9, 0 < w < 10
98  eql x 0             1                               1
99  mul y 0                     0                               0
        From now on we have two r5 values but other variables are the same.

100 add y 25                    25
101 mul y x                     25
102 add y 1                     26
103 mul z y                             r5*26
104 mul y 0                     0
105 add y w                     i6
106 add y 11                    i6+11
107 mul y x                     i6+11
108 add z y                             r5*26+i6+11
-----------------------------------------------------
                w       x       y       z       notes
                i6      1       i6+11   r5*26+i6+11
                                        r6      denote z=r6 (result 6)

109 inp w       i7                              7. input
110 mul x 0             0
111 add x z             r6
112 mod x 26            r6mod26
113 div z 26                            r6/26
114 add x -9            r6mod26-9

Supposing x equaled w on line 79, now
z2 = r6/26 = (z1*26+i6+11)/26 where z1 is given before line 79.

On line 115, x = 1 if r6mod26-9 == i7, and x = 0 otherwise.
Now, r6mod26-9 =
(r5*26+i6+11)mod26-9.

By congruence, the previous line equals (i6+11)mod26-9. Because 0 < i6 < 10,
this is reduced to i6+11-9 = i6+2. Thus, on line 115 x = 1 if i6+2 == i7,
otherwise x = 0.
-------------------------------------------------------------------------------------
                        i6+2 == i7             |        i6+2 != i7
                w       x       y       z      |w       x       y       z       notes
                i7              i6+11   r6/26  |i7              i6+11   r6/26
115 eql x w             1                               0
116 eql x 0             0                               1
117 mul y 0                     0                               0
118 add y 25                    25                              25
119 mul y x                     0                               25
120 add y 1                     1                               26
121 mul z y                             r6/26                           r6/26*26
122 mul y 0                     0                               0
123 add y w                     i7                              i7
124 add y 5                     i7+5                            i7+5
125 mul y x                     0                               i7+5
126 add z y                             r6/26                           r6/26*26+i7+5
-------------------------------------------------------------------------------------
                w       x       y       z      |w       x       y       z       notes
                i7      0       0       r6/26  |i7      1       i7+5    r6/26*26+i7+5
                                        r7                              r7      denote z=r7 (result 7)

127 inp w       i8                              i8                              8. input
128 mul x 0             0                               0
129 add x z             r7                              r7
130 mod x 26            r7mod26                         r7mod26
131 div z 1                             r7                              r7
132 add x 14            r7mod26+14                      r7mod26+14
133 eql x w             0                               0                       x>10, 0 < w < 10
134 eql x 0             1                               1
135 mul y 0                     0                               0
        From now on other variables but z are the same.

136 add y 25                    25
137 mul y x                     25
138 add y 1                     26
139 mul z y                             r7*26
140 mul y 0                     0
141 add y w                     i8
142 add y 16                    i8+16
143 mul y x                     i8+16
144 add z y                             r7*26+i8+16
-----------------------------------------------------
                w       x       y       z       notes
                i8      1       i8+16   r7*26+i8+16
                                        r8      denote z=r8 (result 8)

145 inp w       i9                              9. input
146 mul x 0             0
147 add x z             r8
148 mod x 26            r8mod26
149 div z 1                             r8
150 add x 13            r8mod26+13
151 eql x w             0                       x>10, 0 < w < 10
152 eql x 0             1
153 mul y 0                     0
154 add y 25                    25
155 mul y x                     25
156 add y 1                     26
157 mul z y                             r8*26
158 mul y 0                     0
159 add y w                     i9
160 add y 6                     i9+6
161 mul y x                     i9+6
162 add z y                             r8*26+i9+6
-----------------------------------------------------
                w       x       y       z       notes
                i9      1       i9+6    r8*26+i9+6
                                        r9      denote z=r9 (result 9)

163 inp w       i10                             10. input
164 mul x 0             0
165 add x z             r9
166 mod x 26            r9mod26
167 div z 26                            r9/26
168 add x -14           r9mod26-14

Supposing x equaled w on line 115, now
z3 = r9/26 = ((z2*26+i8+16)*26+i9+6)/26 where z2 is given before line 115.

On line 169, x = 1 if r9mod26-14 == i10, and x = 0 otherwise.
Now, r9mod26-14 =
(r8*26+i9+6)mod26-14.

By congruence, the previous line equals (i9+6)mod26-14. Because 0 < i9 < 10,
this is reduced to i9+6-14 = i9-8. Thus, on line 169 x = 1 if i9-8 == i10,
otherwise x = 0.
-------------------------------------------------------------------------------------
                        i9-8 == i10            |        i9-8 != i10
                w       x       y       z      |w       x       y       z       notes
                i10             i9+6    r9/26  |i10             i9+6    r9/26
169 eql x w             1                               0
170 eql x 0             0                               1
171 mul y 0                     0                               0
172 add y 25                    25                              25
173 mul y x                     0                               25
174 add y 1                     1                               26
175 mul z y                             r9/26                           r9/26*26
176 mul y 0                     0                               0
177 add y w                     i10                             i10
178 add y 15                    i10+15                          i10+15
179 mul y x                     0                               i10+15
180 add z y                             r9/26                           r9/26*26+i10+15
-------------------------------------------------------------------------------------
                w       x       y       z      |w       x       y       z       notes
                i10     0       0       r9/26  |i10     1       i10+15  r9/26*26+i10+15
                                        r10                             r10     denote z=r10 (result 10)

181 inp w       i11                             i11                             11. input
182 mul x 0             0                               0
183 add x z             r10                             r10
184 mod x 26            r10mod26                        r10mod26
185 div z 26                            r10/26                          r10/26
186 add x -11           r10mod26-11                     r10mod26-11

Supposing x equaled w on line 169, now
z4 = r10/26 = z3/26 where z3 is given before line 169.

On line 187, x = 1 if r10mod26-11 == i11, and x = 0 otherwise.
Now, r10mod26-11 =
(r9/26)mod26-11 =
((r8*26+i9+6)/26)mod26-11 -->
(r8+0)mod26-11 -->
(r7*26+i8+16)mod26-11 -->
(i8+16)mod26-11 -->
i8+16-11 -->
i8+5.
Thus, on line 187 x = 1 if i8+5 == i11.
-------------------------------------------------------------------------------------
                        i8+5 == i11            |        i8+5 != i11
                w       x       y       z      |w       x       y       z       notes
                i11             0       r10/26 |i11             i10+15  r10/26

187 eql x w             1                               0
188 eql x 0             0                               1
189 mul y 0                     0                               0
190 add y 25                    25                              25
191 mul y x                     0                               25
192 add y 1                     1                               26
193 mul z y                             r10/26                          r10/26*26
194 mul y 0                     0                               0
195 add y w                     i11                             i11
196 add y 3                     i11+3                           i11+3
197 mul y x                     0                               i11+3
198 add z y                             r10/26                          r10/26*26+i11+3
-------------------------------------------------------------------------------------
                w       x       y       z      |w       x       y       z       notes
                i11     0       0       r10/26 |i11     1       i11+3   r10/26*26+i11+3
                                        r11                             r11     denote z=r11 (result 11)
199 inp w       i12                             i12                             12. input
200 mul x 0             0                               0
201 add x z             r11                             r11
202 mod x 26            r11mod26                        r11mod26
203 div z 26                            r11/26                          r11/26
204 add x -2            r11mod26-2                      r11mod26-2

Supposing x equaled w on line 187, now
z5 = r11/26 = z4/26 where z4 is given before line 187.

On line 205, x = 1 if r11mod26-2 == i12, else x = 0.
Now, r11mod26-2 =
(r10/26)mod26-2 = (((z2*26+i8+16)*26+i9+6)/26/26)mod26-2 =
(z2)mod26-2 = ((z1*26+i6+11)/26)mod26-2 = (z1)mod26-2 =
((((i1+15)*26+i2+10)*26+i3+2))mod26-2 = (i3+2)mod26-2 = i3+2-2 = i3.
Thus, on line 205 x = 1 if i3 == i12.
-------------------------------------------------------------------------------------
                        i3 == i12              |        i3 != i12
                w       x       y       z      |w       x       y       z       notes
                i12             0       r11/26 |i12             i11+3   r11/26
205 eql x w             1                               0
206 eql x 0             0                               1
207 mul y 0                     0                               0
208 add y 25                    25                              25
209 mul y x                     0                               25
210 add y 1                     1                               26
211 mul z y                             r11/26                          r11/26*26
212 mul y 0                     0                               0
213 add y w                     i12                             i12
214 add y 12                    i12+12                          i12+12
215 mul y x                     0                               i12+12
216 add z y                             r11/26                          r11/26+i12+12
-------------------------------------------------------------------------------------
                w       x       y       z      |w       x       y       z       notes
                i12     0       0       r11/26 |i12     1       i12+12  r11/26+i12+12
                                                                                denote z=r12 (result 13)
                                        r12                             r12     denote z=r12 (result 12)
217 inp w       i13                             i13                             13. input
218 mul x 0             0                               0
219 add x z             r12                             r12
220 mod x 26            r12mod26                        r12mod26
221 div z 26                            r12/26                          r12/26
222 add x -16           r12mod26-16                     r12mod26-16

Supposing x equaled w on line 205, now
z6 = r12/26 = z5/26 where z5 is given before line 205.

On line 223, x = 1 if r12mod26-16 == i13, else x = 0.
Now, r12mod26-16 = (r11/26)mod26-16 = (r10/26/26)mod26-16 =
((((i1+15)*26+i2+10)*26+i3+2)/26)mod26-16 = ((i1+15)*26+i2+10)mod26-16 =
(i2+10)mod26-16 = i2+10-16 = i2-6.
Thus, on line 223 x = 1 if i2-6 == i13.
-------------------------------------------------------------------------------------
                        i2-6 == i13            |        i2-6 != i13
                w       x       y       z      |w       x       y       z       notes
                i13             0       r12/26 |i13             i12+12  r12/26
223 eql x w             1                               0
224 eql x 0             0                               1
225 mul y 0                     0                               0
226 add y 25                    25                              25
227 mul y x                     0                               25
228 add y 1                     1                               26
229 mul z y                             r12/26                          r12/26*26
230 mul y 0                     0                               0
231 add y w                     i13                             i13
232 add y 10                    i13+10                          i13+10
233 mul y x                     0                               i13+10
234 add z y                             r12/26                          r12/26*26+i13+10
-------------------------------------------------------------------------------------
                w       x       y       z      |w       x       y       z       notes
                i13     0       0       r12/26 |i13     1       i13+10  r12/26*26+i13+10
                                        r13                             r13     denote z=r13 (result 13)

235 inp w       i14                             i14                             14. input
236 mul x 0             0                               0
237 add x z             r13                             r13
238 mod x 26            r13mod26                        r13mod26
239 div z 26                            r13/26                          r13/26
240 add x -14           r13mod26-14                     r13mod26-14

Supposing x equaled w on line 223, now
z7 = r13/26 = z6/26 where z6 is given before line 223.

On line 223, x = 1 if r13mod26-14 == i14, else x = 0.
Now, r13mod26-14 = (r12/26)mod26-14 = (r11/26/26)mod26-14 =
((((i1+15)*26+i2+10)*26+i3+2)/26/26)mod26-14 =
(((i1+15)*26+i2+10)/26)mod26-14 = (i1+15)mod26-14 = i1+15-14 = i1+1.
Thus, on line 241 x = 1 if i1+1 == i14.
-------------------------------------------------------------------------------------
                        i1+1 == i14            |        i1+1 != i14
                w       x       y       z      |w       x       y       z       notes
                i14             0       r13/26  i14             i13+10  r13/26
241 eql x w             1                               0
242 eql x 0             0                               1
243 mul y 0                     0                               0
244 add y 25                    25                              25
245 mul y x                     0                               25
246 add y 1                     1                               26
247 mul z y                             r13/26                          r13/26*26
248 mul y 0                     0                               0
249 add y w                     i14                             i14
250 add y 13                    i14+13                          i14+13
251 mul y x                     0                               i14+13
252 add z y                             r13/26                          r13/26*26+i14+13
```
