"""ATL ECHO public evidence demo.

Displays selected, previously reported aggregate measurements and ordinary
control comparisons. No ATL ECHO implementation, model weights, source
attribution engine, activation extraction, or proprietary operators included.
"""
from pathlib import Path
import csv

DATA = Path(__file__).resolve().parent / 'data' / 'published_aggregate_metrics.csv'

def load_rows():
    with DATA.open(newline='', encoding='utf-8') as f:
        return {r['condition']: r for r in csv.DictReader(f)}

def main():
    rows = load_rows()
    observed = float(rows['observed']['score'])
    random_mean = float(rows['random_delay_mean']['score'])
    random_p99 = float(rows['random_delay_p99']['score'])
    shuffled_mean = float(rows['shuffled_phase_mean']['score'])
    shuffled_p95 = float(rows['shuffled_phase_p95']['score'])
    shuffled_p = float(rows['shuffled_phase_empirical_p']['score'])
    print('ATL ECHO — public evidence review (aggregate results only)')
    print('Question: does observed temporal structure distinguish itself from controls?')
    print(f'Observed structural score: {observed:.6f}')
    print(f'Random-delay mean:        {random_mean:.6f} | delta: {observed-random_mean:+.6f}')
    print(f'Above random-delay p99:   {observed > random_p99}')
    print(f'Shuffled-phase mean:      {shuffled_mean:.6f} | delta: {observed-shuffled_mean:+.6f}')
    print(f'Above shuffled-phase p95: {observed > shuffled_p95}')
    print(f'Shuffled-phase empirical p (as reported): {shuffled_p:.3f}')
    print('\nInterpretation: the observed score exceeds the random-delay upper tail')
    print('in this recorded evaluation, but does not exceed the shuffled-phase p95.')
    print('These are descriptive re-analyses, not a reproduction of the original runs.')
    print('No claim of cross-domain transfer, physical quantum effects, or AI safety efficacy.')

if __name__ == '__main__':
    main()
