import 'package:flutter/material.dart';

/// Aurora is a background/emphasis layer. The foreground remains semantic
/// and readable when the effect is removed.
class AuroraBackground extends StatelessWidget {
  const AuroraBackground({
    super.key,
    required this.child,
    this.effectsEnabled = true,
  });

  final Widget child;
  final bool effectsEnabled;

  @override
  Widget build(BuildContext context) {
    return Stack(
      fit: StackFit.expand,
      children: [
        const ColoredBox(color: Color(0xFF0D1021)),
        if (effectsEnabled)
          const IgnorePointer(
            ignoring: true,
            child: DecoratedBox(
              decoration: BoxDecoration(
                gradient: RadialGradient(
                  center: Alignment(-0.7, -0.8),
                  radius: 1.15,
                  colors: [
                    Color(0xFF6D5DFC),
                    Color(0x330D1021),
                    Color(0x000D1021),
                  ],
                  stops: [0.0, 0.48, 1.0],
                ),
              ),
            ),
          ),
        child,
      ],
    );
  }
}

class AuroraHeroCard extends StatelessWidget {
  const AuroraHeroCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 0,
      color: Colors.white.withValues(alpha: 0.94),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              'Create something remarkable',
              style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                    color: const Color(0xFF101426),
                    fontWeight: FontWeight.w800,
                  ),
            ),
            const SizedBox(height: 12),
            const Text(
              'The Aurora layer adds atmosphere while the content remains stable and readable.',
              style: TextStyle(color: Color(0xFF526078)),
            ),
            const SizedBox(height: 20),
            FilledButton(
              onPressed: () {},
              child: const Text('Explore'),
            ),
          ],
        ),
      ),
    );
  }
}

class AuroraExample extends StatelessWidget {
  const AuroraExample({super.key, this.effectsEnabled = true});

  final bool effectsEnabled;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: AuroraBackground(
        effectsEnabled: effectsEnabled,
        child: const SafeArea(
          child: Center(
            child: Padding(
              padding: EdgeInsets.all(24),
              child: AuroraHeroCard(),
            ),
          ),
        ),
      ),
    );
  }
}
