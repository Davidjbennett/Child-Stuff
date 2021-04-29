// set.cpp: Stores words and characters

#include <fstream>
#include <iostream>
#include <iterator>
#include <set>
#include <string>
using namespace std;

int main() {
    // Store unique words
    set<string> words;
    string word;
    ifstream ifs("gettysburg.txt");
    while (ifs >> word)
        words.insert(word);

    // Output words and their letters
    for (const string& s: words) {
        cout << s << ": ";
        // Form set of letters
        set<char> letters;
        for (char c: s)
            letters.insert(c);
        copy(begin(letters), end(letters), ostream_iterator<char>(cout, " "));
        cout << endl;
    }
}

/* Output:
--: - 
But,: , B t u 
Four: F o r u 
God,: , G d o 
It: I t 
Liberty,: , L b e i r t y 
Now: N o w 
The: T e h 
We: W e 
a: a 
above: a b e o v 
add: a d 
advanced.: . a c d e n v 
ago: a g o 
all: a l 
altogether: a e g h l o r t 
and: a d n 
any: a n y 
are: a e r 
as: a s 
battle-field: - a b d e f i l t 
be: b e 
before: b e f o r 
birth: b h i r t 
brave: a b e r v 
brought: b g h o r t u 
but: b t u 
by: b y 
can: a c n 
cause: a c e s u 
civil: c i l v 
come: c e m o 
conceived: c d e i n o v 
consecrate: a c e n o r s t 
consecrated: a c d e n o r s t 
continent,: , c e i n o t 
created: a c d e r t 
dead: a d e 
dead,: , a d e 
dedicate: a c d e i t 
dedicated: a c d e i t 
dedicated,: , a c d e i t 
detract.: . a c d e r t 
devotion: d e i n o t v 
did: d i 
died: d e i 
do: d o 
earth.: . a e h r t 
endure.: . d e n r u 
engaged: a d e g n 
equal.: . a e l q u 
far: a f r 
fathers: a e f h r s t 
field,: , d e f i l 
final: a f i l n 
fitting: f g i n t 
for: f o r 
forget: e f g o r t 
forth: f h o r t 
fought: f g h o t u 
freedom: d e f m o r 
from: f m o r 
full: f l u 
gave: a e g v 
government: e g m n o r t v 
great: a e g r t 
ground.: . d g n o r u 
hallow: a h l o w 
have: a e h v 
here: e h r 
here,: , e h r 
here.: . e h r 
highly: g h i l y 
honored: d e h n o r 
in: i n 
increased: a c d e i n r s 
is: i s 
it: i t 
it,: , i t 
larger: a e g l r 
last: a l s t 
little: e i l t 
live.: . e i l v 
lives: e i l s v 
living: g i l n v 
living,: , g i l n v 
long: g l n o 
measure: a e m r s u 
men: e m n 
men,: , e m n 
met: e m t 
might: g h i m t 
nation: a i n o t 
nation,: , a i n o t 
never: e n r v 
new: e n w 
nobly: b l n o y 
nor: n o r 
not: n o t 
note,: , e n o t 
of: f o 
on: n o 
or: o r 
our: o r u 
people,: , e l o p 
perish: e h i p r s 
place: a c e l p 
poor: o p r 
portion: i n o p r t 
power: e o p r w 
proper: e o p r 
proposition: i n o p r s t 
rather: a e h r t 
rather,: , a e h r t 
remaining: a e g i m n r 
remember: b e m r 
resolve: e l o r s v 
resting: e g i n r s t 
say: a s y 
score: c e o r s 
sense,: , e n s 
seven: e n s v 
shall: a h l s 
should: d h l o s u 
so: o s 
struggled: d e g l r s t u 
take: a e k t 
task: a k s t 
testing: e g i n s t 
that: a h t 
the: e h t 
their: e h i r t 
these: e h s t 
they: e h t y 
this: h i s t 
this.: . h i s t 
those: e h o s t 
thus: h s t u 
to: o t 
under: d e n r u 
unfinished: d e f h i n s u 
us: s u 
vain: a i n v 
war,: , a r w 
war.: . a r w 
we: e w 
what: a h t w 
whether: e h r t w 
which: c h i w 
who: h o w 
will: i l w 
work: k o r w 
world: d l o r w 
years: a e r s y 
*/
